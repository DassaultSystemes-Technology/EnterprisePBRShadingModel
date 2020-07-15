import os
import glob
import argparse
import datetime
import imageio
import numpy as np
import jinja2
import importlib

parser = argparse.ArgumentParser(description='Compare images and generate report.')
parser.add_argument('-o', '--out', help='output directory, default: validation_report', default='validation_report')
parser.add_argument('-r', '--ref', help='directory containing reference images, default: reference', default='reference')
parser.add_argument('-i', '--img', help='directory containing result images, default: images', default='images')
parser.add_argument('-t', '--threshold', help='threshold for per-pixel image comparison, default: 0.1', default=0.1)
parser.add_argument('-m', '--tonemapper', help='tonemapping operator, default: simple', default='simple')
parser.add_argument('--ldr', help='force comparison of LDR images', action='store_const', const=True)
args = parser.parse_args()

tonemap = importlib.import_module('tonemap_' + args.tonemapper)

def difference(img, ref):
  diff = img - ref
  diff = np.sqrt(diff * diff)
  diff = np.amax(diff, axis=2)
  rmse = np.mean(diff)
  return diff, rmse

def heatmap(img, threshold):
  img = img * (1/float(threshold))
  colors = np.array([(0,0,1), (0,1,1), (0,1,0), (1,1,0), (1,0,0)])
  idx = np.floor(img * len(colors))
  ip = img * len(colors) - idx
  idx0 = np.clip(idx.astype(int), 0, len(colors)-1)
  idx1 = np.clip(idx.astype(int)+1, 0, len(colors)-1)
  r0 = np.take(colors[:,0], idx0)
  g0 = np.take(colors[:,1], idx0)
  b0 = np.take(colors[:,2], idx0)
  r1 = np.take(colors[:,0], idx1)
  g1 = np.take(colors[:,1], idx1)
  b1 = np.take(colors[:,2], idx1)
  img_r = (1-ip)*r0 + ip*r1
  img_g = (1-ip)*g0 + ip*g1
  img_b = (1-ip)*b0 + ip*b1
  img = np.dstack((img_r, img_g, img_b))
  return img

results = []

for reference in glob.glob(os.path.join(args.ref, '*/*.exr')):
  scene_name = os.path.basename(os.path.dirname(reference))
  image_name = os.path.splitext(os.path.basename(reference))[0]

  print('Working on ' + reference + ' ...')

  outdir = os.path.join(args.out, scene_name)

  outdifffile = os.path.join(outdir, image_name + '-diff.png')
  os.makedirs(outdir, exist_ok=True)

  refdir = os.path.dirname(reference)
  reffile = os.path.basename(reference)
  outreffile = os.path.join(outdir, os.path.splitext(reffile)[0] + '-ref.png')

  imgdir = os.path.join(args.img, os.path.basename(os.path.dirname(reference)))
  imgfile = os.path.basename(reference)
  outimgfile = os.path.join(outdir, os.path.splitext(imgfile)[0] + '-img.png')

  isHDR = os.path.exists(os.path.join(imgdir, imgfile)) and not args.ldr
  if isHDR:
    # load HDR reference and result image
    ref = imageio.imread(os.path.join(refdir, reffile))
    img = imageio.imread(os.path.join(imgdir, imgfile))
  else:
    # load HDR reference image
    ref = imageio.imread(os.path.join(refdir, reffile))

    # tonemap reference image
    ref = tonemap.tonemap(ref)

    # load LDR result image
    imgfile = os.path.splitext(imgfile)[0] + '.png'
    fullpath = os.path.join(imgdir, imgfile)
    if not os.path.exists(fullpath):
      print('File not found: ', fullpath, '\n')
      continue
    
    img = imageio.imread(fullpath)
    img = img[:,:,0:3]
    img = img / 255.

  diff, rmse = difference(img, ref)
  diff = heatmap(diff, args.threshold)

  if isHDR:
    img = tonemap.tonemap(img)
    ref = tonemap.tonemap(ref)

  imageio.imwrite(outdifffile, np.uint8(diff * 255.0))
  imageio.imwrite(outimgfile, np.uint8(img * 255.0))
  imageio.imwrite(outreffile, np.uint8(ref * 255.0))

  results.append({
    'scene': scene_name,
    'name': image_name,
    'rmse': rmse,
    'hdr': isHDR,
    'result': os.path.relpath(outimgfile, args.out),
    'reference': os.path.relpath(outreffile, args.out),
    'difference': os.path.relpath(outdifffile, args.out),
  })

print('Generating report ...')

env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
env.trim_blocks = True
env.lstrip_blocks = True
template = env.get_template('template.j2')
report = template.render(
  results=results,
  threshold=args.threshold,
  ref=args.ref,
  img=args.img,
  created_at=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
with open(os.path.join(args.out, 'index.html'), 'w') as f:
  f.write(report)

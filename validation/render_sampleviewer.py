import os
import glob
import argparse
import subprocess
import shutil

parser = argparse.ArgumentParser(description='Render with the glTF 2.0 Sample Viewer.')
parser.add_argument('sampleviewer', help='/path/to/sampleviewer')
parser.add_argument('-o', '--out', help='output directory, default: images', default='images')
args = parser.parse_args()

for file in glob.glob('scenes/*/*.gltf'):
  scene_type = os.path.basename(os.path.dirname(file))
  image = os.path.join(args.out, scene_type, os.path.basename(file))
  image = os.path.splitext(image)[0]
  os.makedirs(os.path.dirname(image), exist_ok=True)

  print('Rendering ' + file + '...')

  subprocess.run(['npm', 'run', 'start-offscreen', '--', '--', '--dimensions', '400', '400', '--camera-index', '0', os.path.abspath(file)], cwd=args.sampleviewer, shell=True)
  shutil.copyfile(os.path.join(args.sampleviewer, 'output.png'), image + '.png')

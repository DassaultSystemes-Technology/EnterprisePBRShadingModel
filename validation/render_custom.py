import os
import glob
import argparse
from PIL import Image

parser = argparse.ArgumentParser(description='Render images from glTF files.')
parser.add_argument('-o', '--out', help='output directory, default: images', default='images')
args = parser.parse_args()

for file in glob.glob('scenes/*/*.gltf'):
  scene_type = os.path.basename(os.path.dirname(file))
  image = os.path.join(args.out, scene_type, os.path.basename(file))
  image = os.path.splitext(image)[0]
  os.makedirs(os.path.dirname(image), exist_ok=True)

  print('Rendering ' + file + '...')
  
  # TODO: Add your render call here. Output name: image + '.png'.
  
  f = Image.new('RGB', size=(400, 400))
  f.save(image + '.png')

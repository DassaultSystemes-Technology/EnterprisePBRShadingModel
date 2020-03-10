import numpy as np

def tonemap(f):
  return np.clip(np.power(f, 1 / 2.2), 0, 1)

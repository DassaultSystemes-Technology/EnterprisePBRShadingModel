import numpy as np

def tonemap(f):
  return np.power(f / (1 + f), 1 / 2.2)

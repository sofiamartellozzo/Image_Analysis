import numpy as np

def infimum(I1, I2):

  shape = I1.shape

  nrows = img1.shape[0]
  ncols = img1.shape[1]

  output = np.zeros(shape)

  for i in range(nrows):
    for j in range(ncols):
      if I1[i][j] <= I2[i][j]:
        output[i][j] = I1[i][j]
      else:
        output[i][j] = I2[i][j]

  return output
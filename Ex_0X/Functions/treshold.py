import numpy as np

def treshold(treshold, input_img):

  nrows = input_img.shape[0]
  ncols = input_img.shape[1]
  output_img = np.zeros((nrows, ncols))

  for i in range(nrows):
    for j in range(ncols):

      if input_img[i][j] >= treshold:
        output_img[i][j] = 255

  return output_img
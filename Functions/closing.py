from Functions.erosion import erosion
from Functions.dilation import dilation


# CLOSING = dilation and then erosion
def closing(input_img, i):
  step1 = dilation(input_img, i)
  step2 = erosion(step1, i)
  return step2
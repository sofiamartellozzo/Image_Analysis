from Functions.erosion import erosion
from Functions.dilation import dilation


# OPENING = erosion and then dilation
def opening(input_img, i):
  step1 = erosion(input_img, i)
  step2 = dilation(step1, i)
  return step2
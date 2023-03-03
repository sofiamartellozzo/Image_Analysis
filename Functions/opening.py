import erosion as e
import dilation as d

def opening(input_img, i):
  step1 = e.erosion(input_img, i)
  step2 = d.dilation(step1, i)
  return step2
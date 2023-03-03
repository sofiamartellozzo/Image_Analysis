import erosion as e
import dilation as d

def closing(input_img, i):
  step1 = d.dilation(input_img, i)
  step2 = e.erosion(step1, i)
  return step2
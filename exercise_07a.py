import cv2
import numpy as np

from Functions.compare import compare
from Functions.openClose import openClose

input_img = cv2.imread("img/cam_74.pgm", cv2.IMREAD_GRAYSCALE)

out1 = openClose(input_img, 2)

out2 = openClose(out1, 2)

print(compare(out1, out2))
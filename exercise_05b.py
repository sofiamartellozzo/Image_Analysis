import cv2
import numpy as np

from Functions.compare import compare
from Functions.closing import closing

out1 = cv2.imread("outputs/exercise_04b_output_02.pgm", cv2.IMREAD_GRAYSCALE)

out2 = closing(out1, 2)

print(compare(out1, out2))
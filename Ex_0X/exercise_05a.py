import cv2
import numpy as np

from Functions.compare import compare
from Functions.opening import opening

out1 = cv2.imread("outputs/exercise_04a_output_01.pgm", cv2.IMREAD_GRAYSCALE)

out2 = opening(out1, 1)

print(compare(out1, out2))
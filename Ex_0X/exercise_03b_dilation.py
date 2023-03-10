import cv2
import numpy as np
from Functions.dilation import dilation
from Functions.compare import compare

input_img = cv2.imread("img/immed_gray_inv.pgm", cv2.IMREAD_GRAYSCALE)

out1 = dilation(input_img, 1)

print("Saving image to file pgm ...")
cv2.imwrite("outputs/exercise_03b_output_01.pgm", out1);

print("Showing image in window")
cv2.imshow("Window: dilation 1", out1)

out2 = dilation(input_img, 2)

print("Saving image to file pgm ...")
cv2.imwrite("outputs/exercise_03b_output_02.pgm", out2);

print("Showing image in window")
cv2.imshow("Window: dilation 2", out2)

true_output1 = cv2.imread("img/immed_gray_inv_20051123_dil1.pgm", cv2.IMREAD_GRAYSCALE)
true_output2 = cv2.imread("img/immed_gray_inv_20051123_dil2.pgm", cv2.IMREAD_GRAYSCALE)

print(compare(true_output1, out1))
print(compare(true_output2, out2))

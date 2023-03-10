import cv2
import numpy as np
from Functions.opening import opening
from Functions.compare import compare

input_img = cv2.imread("img/immed_gray_inv.pgm", cv2.IMREAD_GRAYSCALE)

out_1 = opening(input_img, 1)

print("Saving image to file pgm ...")
cv2.imwrite("outputs/exercise_04a_output_01.pgm", out_1);

print("Showing image in window")
cv2.imshow("Window: opening 1", out_1)

out_2 = opening(input_img, 2)

print("Saving image to file pgm ...")
cv2.imwrite("outputs/exercise_04a_output_02.pgm", out_2);

print("Showing image in window")
cv2.imshow("Window: opening 2", out_2)

true_output1 = cv2.imread("img/immed_gray_inv_20051123_ope1.pgm", cv2.IMREAD_GRAYSCALE)
true_output2 = cv2.imread("img/immed_gray_inv_20051123_ope2.pgm", cv2.IMREAD_GRAYSCALE)

print(compare(true_output1, out_1))
print(compare(true_output2, out_2))

import cv2
import numpy as np
from Functions.closing import closing
from Functions.compare import compare

input_img = cv2.imread("img/immed_gray_inv.pgm", cv2.IMREAD_GRAYSCALE)

out_1 = closing(input_img, 1)

print("Saving image to file pgm ...")
cv2.imwrite("outputs/exercise_04b_output_01.pgm", out_1);

print("Showing image in window")
cv2.imshow("Window: closing 1", out_1)

out_2 = closing(input_img, 2)

print("Saving image to file pgm ...")
cv2.imwrite("outputs/exercise_04b_output_02.pgm", out_2);

print("Showing image in window")
cv2.imshow("Window: closing 2", out_2)

true_output1 = cv2.imread("img/immed_gray_inv_20051123_clo1.pgm", cv2.IMREAD_GRAYSCALE)
true_output2 = cv2.imread("img/immed_gray_inv_20051123_clo2.pgm", cv2.IMREAD_GRAYSCALE)

print(compare(true_output1, out_1))
print(compare(true_output2, out_2))

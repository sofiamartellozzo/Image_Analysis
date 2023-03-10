import cv2

from Functions.openClose import openClose
from Functions.compare import compare

input_img = cv2.imread("img/immed_gray_inv.pgm", cv2.IMREAD_GRAYSCALE)

step2_1 = openClose(input_img, 2)

print("Saving image to file pgm ...")
cv2.imwrite("outputs/exercise_06a_output_01.pgm", step2_1);

print("Showing image in window")
cv2.imshow("Window: closing(opening()) 1", step2_1)

step2_2 = openClose(input_img, 4)

print("Saving image to file pgm ...")
cv2.imwrite("outputs/exercise_06a_output_02.pgm", step2_2);

print("Showing image in window")
cv2.imshow("Window: closing(opening()) 2", step2_2)

#check the results
true_output1 = cv2.imread("img/immed_gray_inv_20051123_clo2ope2.pgm", cv2.IMREAD_GRAYSCALE)
true_output2 = cv2.imread("img/immed_gray_inv_20051123_clo4ope4.pgm", cv2.IMREAD_GRAYSCALE)

print(compare(true_output1, step2_1))
print(compare(true_output2, step2_2))

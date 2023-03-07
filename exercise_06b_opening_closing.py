import cv2

from Functions.closeOpen import closeOpen
from Functions.compare import compare

input_img = cv2.imread("img/immed_gray_inv.pgm", cv2.IMREAD_GRAYSCALE)

step2_1 = closeOpen(input_img, 2)

print("Saving image to file pgm ...")
cv2.imwrite("outputs/exercise_06b_output_01.pgm", step2_1);

print("Showing image in window")
cv2.imshow("Window: opening(closing()) 1", step2_1)

step2_2 = closeOpen(input_img, 4)

print("Saving image to file pgm ...")
cv2.imwrite("outputs/exercise_06b_output_02.pgm", step2_2);

print("Showing image in window")
cv2.imshow("Window: opening(closing()) 2", step2_2)

#check the results
true_output1 = cv2.imread("img/immed_gray_inv_20051123_ope2clo2.pgm", cv2.IMREAD_GRAYSCALE)
true_output2 = cv2.imread("img/immed_gray_inv_20051123_ope4clo4.pgm", cv2.IMREAD_GRAYSCALE)

print(compare(true_output1, step2_1))
print(compare(true_output2, step2_2))

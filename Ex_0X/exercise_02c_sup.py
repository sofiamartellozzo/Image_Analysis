import cv2
import numpy as np
from Functions.sup import supremum
from Functions.inf import infimum
from Functions.compare import compare

img1 = cv2.imread("img/image1.pgm", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("img/image2.pgm", cv2.IMREAD_GRAYSCALE)

out_sup = supremum(img1, img2)

print("Saving image to file pgm ...")
cv2.imwrite("outputs/exercise_02c_output_01.pgm", out_sup);

print("Showing image in window")
cv2.imshow("Window: sup", out_sup)


out_inf = infimum(img1, img2)

print("Saving image to file pgm ...")
cv2.imwrite("outputs/exercise_02c_output_02.pgm", out_inf);

print("Showing image in window... Press a key to finish.")
cv2.imshow("Window: inf", out_inf)

true1 = cv2.imread("img/image1_sup_image2.pgm", cv2.IMREAD_GRAYSCALE)
true2 = cv2.imread("img/image1_inf_image2.pgm", cv2.IMREAD_GRAYSCALE)

print(compare(true1,out_sup))
print(compare(true2, out_inf))


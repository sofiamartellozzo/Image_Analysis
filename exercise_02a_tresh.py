# import libraries
import cv2
import numpy as np

from Functions.treshold import treshold 

input_img = cv2.imread("img/cam_74.pgm", cv2.IMREAD_GRAYSCALE)

print(input_img.shape)

nrows = input_img.shape[0]
ncols = input_img.shape[1]
print(nrows, ncols)

output_img = treshold(100, input_img)

print("Saving image to file pgm ...")
cv2.imwrite("outputs/exercise_02a_output_01.pgm", output_img);

print("Showing image in window... Press a key to finish.")
cv2.imshow("Window: tresh100", output_img)
cv2.waitKey(0) # waiting for a key

cv2.destroyAllWindows()
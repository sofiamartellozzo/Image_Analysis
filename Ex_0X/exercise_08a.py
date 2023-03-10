import cv2

from Functions.opening import opening
from Functions.closing import closing
from Functions.openClose import openClose
from Functions.closeOpen import closeOpen

input_img = cv2.imread("img/isn_256.pgm",cv2.IMREAD_GRAYSCALE )

filter1 = opening(input_img, 1)
cv2.imwrite("outputs/exercise_08a_output_01.pgm", filter1);
cv2.imshow("Window: opening", filter1)

filter2 = closing(input_img, 1)
cv2.imwrite("outputs/exercise_08a_output_02.pgm", filter2);
cv2.imshow("Window: closing", filter2)

filter3 = openClose(input_img, 1)
cv2.imwrite("outputs/exercise_08a_output_03_best1.pgm", filter3);
cv2.imshow("Window: opening(closing())", filter3)

filter4 = closeOpen(input_img, 1)
cv2.imwrite("outputs/exercise_08a_output_04_best2.pgm", filter4);
cv2.imshow("Window: closing(opening())", filter4)

file1 = open('outputs/exercise_08a_output_01.txt', 'w')
file1.write('3\n4')
file1.close()


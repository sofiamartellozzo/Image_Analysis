import cv2
from Functions.compare import compare

img1 = cv2.imread("img/cam_74.pgm", cv2.IMREAD_GRAYSCALE)

img2 = cv2.imread("img/cam_74_threshold100.pgm", cv2.IMREAD_GRAYSCALE)

out1 = compare(img1, img1)
print("Save the first results in a txt file")

file1 = open('outputs/exercise_02b_output_01.txt', 'w')
file1.write(str(out1))
file1.close()

out2 = compare(img1, img2)
print("Save the second results in a txt file")

file2 = open('outputs/exercise_02b_output_02.txt', 'w')
file2.write(str(out2))
file2.close()
import cv2

from Functions.opening import opening
from Functions.closing import closing

def closeOpen(img, i):
    step1 = closing(img, i)
    step2 = opening(step1, i)
    return step2
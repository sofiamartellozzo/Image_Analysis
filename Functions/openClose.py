import cv2

from Functions.opening import opening
from Functions.closing import closing

def openClose(img, i):
    step1 = opening(img, i)
    step2 = closing(step1, i)
    return step2
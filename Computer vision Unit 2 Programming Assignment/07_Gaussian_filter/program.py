import cv2
import numpy as np

img = cv2.imread("input.jpg")
gaussian = cv2.GaussianBlur(img, (9, 9), 0)
cv2.imwrite("output.png", gaussian)
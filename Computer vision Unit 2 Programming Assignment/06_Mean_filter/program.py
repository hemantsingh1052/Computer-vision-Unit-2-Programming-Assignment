import cv2
import numpy as np

img = cv2.imread("input.jpg")
mean = cv2.blur(img, (9, 9))
cv2.imwrite("output.jpg", mean)
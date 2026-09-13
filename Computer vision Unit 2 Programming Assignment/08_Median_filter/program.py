import cv2
import numpy as np

img = cv2.imread("input.jpg")
median = cv2.medianBlur(img, 9)
cv2.imwrite("output.png", median)
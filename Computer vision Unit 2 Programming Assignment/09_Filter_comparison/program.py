import cv2
import numpy as np

img = cv2.imread("input.jpg")

mean = cv2.blur(img, (9, 9))
gaussian = cv2.GaussianBlur(img, (9, 9), 0)
median = cv2.medianBlur(img, 9)

cv2.imwrite("output_mean.png", mean)
cv2.imwrite("output_gaussian.png", gaussian)
cv2.imwrite("output_median.png", median)
import cv2
import numpy as np

img = cv2.imread("input.jpg", 0)

kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
sharpened_image = cv2.filter2D(img, -1, kernel)

cv2.imwrite("output.png", sharpened_image)
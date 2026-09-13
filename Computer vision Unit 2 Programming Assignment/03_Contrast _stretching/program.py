import cv2
import numpy as np

img = cv2.imread("input.jpg")
greyscale = cv2.imread("input.jpg", 0)
min = np.min(greyscale)
max = np.max(greyscale)
strech = (greyscale - min) * (255.0 / (max - min))
strech = strech.astype(np.uint8)
cv2.imwrite("input.jpeg", greyscale)
cv2.imwrite("output.png", strech)
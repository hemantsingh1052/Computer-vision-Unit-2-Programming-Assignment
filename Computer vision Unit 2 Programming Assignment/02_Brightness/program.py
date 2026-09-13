import cv2
import numpy as np
img = cv2.imread("input.jpg")
brightness = 50
x,y = 100, 100
before = img[x,y].copy ()
print(before)
enhance_image = np.clip(img.astype(np.int16) + brightness, 0, 255).astype(np.uint8)
after = enhance_image[x,y]
print("pixel value before enhancement: ", before)
print("pixel value after enhancement: ", after)

cv2.imwrite("output.png", enhance_image)



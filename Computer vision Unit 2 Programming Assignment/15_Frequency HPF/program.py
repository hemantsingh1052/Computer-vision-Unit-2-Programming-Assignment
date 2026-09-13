import cv2
import numpy as np

img = cv2.imread("input.jpg", 0)
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
rows, cols = img.shape
crow = rows // 2
ccols = cols // 2
mask = np.ones((rows, cols, 2), np.uint8)
r = 30
mask[crow - r : crow + r, ccols - r : ccols + r] = 0
filter_dftshift = dft_shift * mask
inverse_shift = np.fft.ifftshift(filter_dftshift)
img_back = cv2.idft(inverse_shift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
cv2.imwrite("output.png", img_back)
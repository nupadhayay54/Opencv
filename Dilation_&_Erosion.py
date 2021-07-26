import cv2
import numpy as np
img = cv2.imread('Temple.jpg', 1)
kernel = np.ones((2, 2), np.uint8)
# Erosion
img_erosion = cv2.erode(img, kernel, iterations=1)
# Dilation
img_dilation = cv2.dilate(img, kernel, iterations=1)
# Original image show
cv2.imshow('Original', img)
# Erosion show
cv2.imshow('Erosion', img_erosion)
# Dilation show
cv2.imshow('Dilation', img_dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()
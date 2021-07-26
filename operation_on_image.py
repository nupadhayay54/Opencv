import cv2
import numpy as np

img = cv2.imread('Temple.jpg', 1)
# Blur
avging = cv2.blur(img, (10, 10))
cv2.imshow('Averaging', avging)
cv2.waitKey(0)
Blur = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow('Gaussian Blurring', Blur)
Bilateral_Filter = cv2.bilateralFilter(img, 9, 75, 75)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Sharpen
sharpening_filter = np.array([[-1, -1, -1],
                              [-1, 9, -1],
                              [-1, -1, -1]])
sharpened_image = cv2.filter2D(img, -1, sharpening_filter)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Edge detection
canny = cv2.Canny(img, 20, 170)
cv2.imshow('Original Image', img)
cv2.imshow('Canny Edge', canny)
cv2.waitKey(0)

import cv2
import numpy as np
img = cv2.imread('flower.jpg')
# Translation
num_rows, num_cols = img.shape[:2]
translation_matrix = np.float32([[1, 0, 70], [0, 1, 110]])
img_translation = cv2.warpAffine(img, translation_matrix, (num_cols, num_rows))
cv2.imshow('Translation', img_translation)
cv2.imshow('Original image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Rotation
image = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Rotational Image', image)
cv2.imshow('Original window', img)
cv2.waitKey(0)
# Cropping
imgCropped = img[:320, :320]
cv2.imshow("Cropped image", imgCropped)
cv2.imshow("Original image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Scaling
print('Original Dimension: ', img.shape)
scale_percent = 60
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dimension = (width, height)
resized = cv2.resize(img, dimension, interpolation=cv2.INTER_AREA)
print('Resized Dimensions: ', resized.shape)
cv2.imshow('Resized image', resized)
cv2.imshow('Original image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



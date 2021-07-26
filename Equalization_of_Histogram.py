import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('flower.jpg')
cv.imshow('flower', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Applying histogram equalization on grayscale image
eq_gray = cv.equalizeHist(gray)
cv.imshow('Equalized Histogram of a grayscale image', eq_gray)

# Applying histogram equalization on Color image
# covert from RGB colo-space to YCrCb
ycrcb_img = cv.cvtColor(img, cv.COLOR_BGR2YCrCb)
# equalize the histogram of the Y channel
ycrcb_img[:, :, 0] = cv.equalizeHist(ycrcb_img[:, :, 0])

# convert back to RGB color-space from YCrCb
eq_img = cv.cvtColor(ycrcb_img, cv.COLOR_YCrCb2BGR)
cv.imshow('Equalized Histogram of colored image', eq_img)

# Color Histogram
r, g, b = cv.split(img)

# Histogram plotting for grayscale image
fig1 = plt.figure(1)
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.hist(gray.ravel(), 256, [0, 256])

# Histogram plotting for colored image
fig2 = plt.figure(2)
plt.hist(r.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 256, [0, 256])
plt.hist(b.ravel(), 256, [0, 256])
plt.title('Colored Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.show()

cv.waitKey()

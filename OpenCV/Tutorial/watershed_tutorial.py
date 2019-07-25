import cv2
import numpy as np
import matplotlib.pyplot as plt


def display(img, cmap='gray'):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(1, 1, 1)  # also same with ax = fig.add_subplot(111)
    ax.imshow(img, cmap='gray')
    plt.pause(1)


sep_coins = cv2.imread('DATA/pennies.jpg')
display(sep_coins)

# Median Blur
# Grayscale
# Binary Threshold
# Find Contours

sep_blur = cv2.medianBlur(sep_coins, 25)
display(sep_blur)

gray_sep_coins = cv2.cvtColor(sep_blur, cv2.COLOR_BGR2GRAY)
display(gray_sep_coins)

ret, sep_thresh = cv2.threshold(gray_sep_coins, 160, 255, cv2.THRESH_BINARY_INV)
display(sep_thresh)

image, contours, hierarchy = cv2.findContours(sep_thresh.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(sep_coins, contours, i, (255, 0, 0), 10)

# Going to display pennies contours with color of red
display(sep_coins)


# Better Performance

img = cv2.imread('DATA/pennies.jpg')
img = cv2.medianBlur(img, 35)

# Blurred
display(img)

# OTSU THRESHOLDING
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

display(thresh)

# NOISE REMOVAL (OPTIONAL)
kernel = np.ones((3, 3), np.uint8)

opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
display(opening)

# Euclidean Distance Transform
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
display(dist_transform)
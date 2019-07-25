import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load two images
img1 = cv2.imread('../DATA/dog_backpack.png')
img2 = cv2.imread('../DATA/watermark_no_copy.png')

img2 = cv2.resize(img2, (600, 600))

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

plt.imshow(img1)
plt.pause(1)

plt.imshow(img2)
plt.pause(1)

img1.shape

x_offset = 934-600
y_offset = 1401-600

# Creating an ROI of the same size of the foreground image (smaller image that will go on top)
rows, cols, channels = img2.shape
# roi = img1[0:rows, 0:cols ] # TOP LEFT CORNER
roi = img1[y_offset:1401, x_offset:943]  # BOTTOM RIGHT CORNER

plt.title("ROI")
plt.imshow(roi)
plt.pause(1)
plt.title("")

roi.shape

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

img2gray.shape

plt.imshow(img2gray, cmap='gray')
plt.pause(1)

mask_inv = cv2.bitwise_not(img2gray)
mask_inv.shape

plt.imshow(mask_inv, cmap='gray')
plt.pause(1)

#  Convert Mask to have 3 channels
white_background = np.full(img2.shape, 255, dtype=np.uint8)
bk = cv2.bitwise_or(white_background, white_background, mask=mask_inv)
bk.shape

plt.imshow(bk)
plt.pause(1)

# Grab Original FG image and place on top of Mask
plt.imshow(mask_inv, cmap='gray')
plt.pause(1)

fg = cv2.bitwise_or(img2, img2, mask=mask_inv)
plt.imshow(fg)
plt.pause(1)

fg.shape

# Get ROI and blend in the mask with the ROI

final_roi = cv2.bitwise_or(roi, fg)
plt.imshow(final_roi)

large_img = img1
small_img = final_roi

large_img[y_offset:y_offset+small_img.shape[0], x_offset:x_offset+small_img.shape[1]] = small_img

plt.title("Final")
plt.imshow(large_img)
plt.pause(1)


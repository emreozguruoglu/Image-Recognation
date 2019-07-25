import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('DATA/sammy_face.jpg')

plt.imshow(img)
plt.pause(1)

edges = cv2.Canny(image=img, threshold1=0, threshold2=255)

plt.imshow(edges)
plt.pause(1)

med_val = np.median(img)

print(med_val)

# LOWER THRESHOLD TO EITHER 0 OR 70% OF THE MEDIAN VALUE, WHICHEVER IS GREATER
lower = int(max(0, 0.7 * med_val))

# UPPER THRESHOLD TO EITHER %130 OF THE MEDIAN OR THE MAX 255, WHICHEVER IS SMALLER
upper = int(min(255, 1.3 * med_val))

edges= cv2.Canny(image=img, threshold1=lower, threshold2=upper+100)
plt.imshow(edges)

plt.pause(1)

# CLEARING THE NOISES
blurred_image = cv2.blur(img, ksize=(7, 7))

edges = cv2.Canny(image=blurred_image, threshold1=lower, threshold2=upper)
plt.imshow(edges)
plt.pause(1)


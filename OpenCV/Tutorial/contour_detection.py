import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('DATA/internal_external.png', 0)
plt.imshow(img)
plt.pause(1)

plt.imshow(img, cmap='gray')
plt.pause(1)

ret, threshold = cv2.threshold(img, 127, 255, 0)
contours, hierarchy = cv2.findContours(threshold, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

external_contours = np.zeros(threshold.shape)

# list(range(len(contours)))

for i in range(len(contours)):
    # EXTERNAL CONTOUR --> Şekilleri gösterir
    if hierarchy[0][i][3] == -1: # Eşitlik değeri değiştirilerek sadece yuvarlaklar veya çizgiler seçilebilir.
        cv2.drawContours(external_contours, contours, i, 255, -1)

    # INTERNAL CONTOUR --> Şekillerin içindekileri gösterir
    # if hierarchy[0][i][3] != -1:
    #   cv2.drawContours(external_contours, contours, i, 255, -1)

# Contours
plt.imshow(external_contours, cmap='gray')
plt.pause(1)



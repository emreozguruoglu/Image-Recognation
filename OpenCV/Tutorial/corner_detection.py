import cv2
import numpy as np
import matplotlib.pyplot as plt

flat_chess = cv2.imread('DATA/flat_chessboard.png')

flat_chess= cv2.cvtColor(flat_chess, cv2.COLOR_BGR2RGB)

plt.imshow(flat_chess)
plt.pause(1)

gray_flat_chess = cv2.cvtColor(flat_chess, cv2.COLOR_BGR2GRAY)

plt.imshow(gray_flat_chess, cmap='gray')
plt.pause(1)

real_chess = cv2.imread('DATA/real_chessboard.jpg')

real_chess = cv2.cvtColor(real_chess, cv2.COLOR_BGR2RGB)


plt.imshow(real_chess)
plt.pause(1)

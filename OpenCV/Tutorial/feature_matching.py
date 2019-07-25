# NEED FIX

import cv2
import matplotlib.pyplot as plt

def display(img):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap='gray')


reeses = cv2.imread('DATA/reeses_puffs.png', 0)

display(reeses)
plt.pause(1)

cereals = cv2.imread('DATA/many_cereals.jpg',0)

display(cereals)
plt.pause(1)


# Brute Force Detection

orb = cv2.ORB_create()  # detector object
kp1, des1 = orb.detectAndCompute(reeses, None)
kp2, des2 = orb.detectAndCompute(cereals, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1, des2)

matches = sorted(matches, key=lambda x: x.distance)

# single_match = matches[0]
# print(single_match.distance)

reeses_matches = cv2.drawMatches(reeses, kp1, cereals, kp2, matches[:25], None, flags=2)

display(reeses_matches)
plt.pause(1)

sift = cv2.xfeatures2d.SIFT_create()

kp1, des1 = sift.detectAndCompute(reeses, None)
kp2, des2 = sift.detectAndCompute(cereals, None)

bf = cv2.BFMatcher()

matches = bf.knnMatch(des1, des2, k=2)

good = []

# LESS DISTANCE  == BETTER MATCH

# RATIO MATCH1 < 75% MATCH 2
for match1, match2 in matches:
    # IF MATCH 1 DISTANCE si LESS THAN 75% of MATCH of 2 DISTANCE
    # THEN DESCRIPTOR WAS A GOOD MATCH, LETS KEEP IT!
    if match1.distance < 0.75*match2.distance:
        good.append([match1])

sift_matches = cv2.drawMatchesKnn(reeses, kp1, cereals, kp2, good, None, flags=2)

display(sift_matches)
plt.pause(2)

sift = cv2.xfeatures2d.SIFT_create()

kp1, des1 = sift.detectAndCompute(reeses, None)
kp2, des2 = sift.detectAndCompute(cereals, None)

# FLANN
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)

flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1, des2, k=2)

good = []

for match1, match2 in matches:
    if match1.distance < 0.7*match2.distance:
        good.append(match1)

flann_matches = cv2.drawMatchesKnn(reeses, kp1, cereals, kp2, good, None, flags=0)
display(flann_matches)
plt.pause(2)


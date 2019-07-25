import cv2
import  matplotlib.pyplot as plt


full = cv2.imread('DATA/sammy.jpg')
full = cv2.cvtColor(full, cv2.COLOR_BGR2RGB)

plt.title("Sammy")
plt.imshow(full)
plt.pause(1)

face = cv2.imread('DATA/sammy_face.jpg')
face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)

plt.title("Sammy Face")
plt.imshow(face)
plt.pause(1)

# All the 6 methods for comparion in a list
# Note how we are using strings, later on we'll use the eval() function to convert to function

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for m in methods:
    # CREATE A COPY
    full_copy = full.copy()

    method = eval(m)

    # Template Matching

    res = cv2.matchTemplate(full_copy, face, method)

    min_val, max_val, min_location, max_location = cv2.minMaxLoc(res)

    if method  in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_location  # (x,y)
    else:
        top_left = max_location

    height, width, channels = face.shape

    bottom_right = (top_left[0] + width, top_left[1]+height)

    cv2.rectangle(full_copy, top_left, bottom_right, (255, 0, 0), 10)

    # PLOT AND SHOW THE IMAGES

    plt.subplot(121) # 1 row , 2 colomns
    plt.imshow(res)

    plt.pause(1)
    plt.title('HEATMAP OF TEMPLATE MATCHING')

    plt.subplot(122)
    plt.imshow(full_copy)

    plt.pause(1)
    plt.title('DETECTION OF TEMPLATE')

    # TITLE WITH THE METHOD USED
    plt.suptitle(m)
    plt.show()

    plt.pause(1)

    print('\n')
    print('\n')

#my_method = eval('cv2.TM_CCOEFF')
#res = cv2.matchTemplate(full, face, cv2.TM_CCOEFF,my_method)

#plt.imshow(res)
#plt.pause(1)
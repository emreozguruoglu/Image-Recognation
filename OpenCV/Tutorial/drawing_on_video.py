import cv2

# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# TOP LEFT CORNER
# x = width // 2
# y = height // 2

# WIDTH AND HEIGHT OF RECTANGLE
# w = width // 4
# h = height // 4

# BOTTOM RIGHT x+w, y+h


# CALLBACK FUNCTION RECTANGLE


def draw_rectangle(event, x, y, flags, param):
    global pt1, pt2, topLeft_clicked, botRight_clicked

    if event is cv2.EVENT_LBUTTONDOWN:

        # RESET THE RECTANGLE (IT CHECKS IF THE RECT THERE)
        if topLeft_clicked is True and botRight_clicked is True:
            pt1 = (0, 0)
            pt2 = (0, 0)
            topLeft_clicked = False
            botRight_clicked = False

        if topLeft_clicked is False:
            pt1 = (x, y)
            topLeft_clicked = True

        elif botRight_clicked is False:
            pt2 = (x, y)
            botRight_clicked = True

# GLOBAL VARIABLES


pt1 = (0, 0)
pt2 = (0, 0)
topLeft_clicked = False
botRight_clicked = False

# CONNECT TO THE CALLBACK
cap = cv2.VideoCapture(0)

cv2.namedWindow('Test')
cv2.setMouseCallback('Test', draw_rectangle)

while True:
    ret, frame = cap.read()

    # DRAWING ON THE FRAME BASED OFF THE GLOBAL VARIABLES
    if topLeft_clicked is True:
        cv2.circle(frame, center=pt1, radius=5, color=(0, 0, 255), thickness=-11)

    if topLeft_clicked and botRight_clicked:
        cv2.rectangle(frame, pt1, pt2, (0, 0, 255), 3)

    # Sadece boş yuvarlak halka
    # if topLeft_clicked is True:
        # cv2.circle(frame, center=pt1, radius=50, color=(0, 0, 255), thickness=5)

    # cv2.rectangle(frame, (x, y), (x+w,y+h), color=(0,0,255),thickness=4)
    cv2.imshow('Test', frame)

    if cv2.waitKey(1) & 0xFF is ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


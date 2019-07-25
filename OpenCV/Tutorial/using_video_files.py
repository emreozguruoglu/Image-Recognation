import cv2
import time

# video dosyası dizini verilecek.
cap = cv2.VideoCapture("myfirstvideo.mp4")

#  Dosya bulunamazsa hata veriliyor.
if cap.isOpened() is False:
    print('ERROR FILE NOT FOUND OR WRONG CODEC USED!')

while cap.isOpened():
    ret, frame = cap.read()

    if ret is True:
        # WRITER 20 FPS
        time.sleep(1/20)
        cv2.imshow('frame', frame)

        if cv2.waitKey(10) & 0xFF is ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
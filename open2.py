import cv2
cap = cv2.VideoCapture('myvideo.mkv')

while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        cv2.imshow('frame', frame)
        if cv2.waitKey(15) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()

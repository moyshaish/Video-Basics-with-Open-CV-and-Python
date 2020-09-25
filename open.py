import cv2
cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
output = cv2.VideoWriter("myvideo.mkv",cv2.VideoWriter_fourcc(*'DIVX'),20,(width, height))
while True:
    ret, frame = cap.read()
    output.write(frame)

    cv2.imshow('frame',frame)

    if cv2.waitkey(5) & 0xFF == 27:
        break

cap.release()
output.release()
cv2.distroyAllWindows()

import cv2

def draw_rectangle(event,x,y,flags,param):


    global pt1, pt2 , top_left_clicked, bottom_right_clicked

    if event == cv2.EVENT_LBUTTONDOWN:
        if tope_left_clicked == True and bottom_right_clicked== True:
            pt1 = (0,0)
            pt2 = (0,0)

            tope_left_clicked = False
            bottom_right_clicked = False

    if top_left_clicked == False:
        pt1 = (x,y)
        top_left_clicked = True

pt1 = (0,0)
pt2 = (0,0)

top_left_clicked = False
bottom_right_clicked = False

cap = cv2.VideoCapture(0)

cv2.namedWindow('Test')

cv2.setMouseCallback('Test',draw_rectangle)

while True:
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if top_left_clicked == True:
        cv2.circle(frame,center=pt1,radius=5,color=(255,0,255),thickness=-1)

    if top_left_clicked == True and bottom_right_clicked == True:
        cv2.rectangle(frame, pt1,pt2,(0,0,255),3)

    if cv2.waitKey(3) & 0xff==27:
        break
cap.release()
cv2.distroyWindows()

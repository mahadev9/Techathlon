import cv2
import numpy as np

def nothing(x):
    pass

cap=cv2.VideoCapture("G:\Pot Hole\Flight02.mp4")
cv2.namedWindow('res')
cv2.createTrackbar('b_higher','res',0,255,nothing)
cv2.createTrackbar('g_higher','res',0,255,nothing)
cv2.createTrackbar('r_higher','res',0,255,nothing)
cv2.createTrackbar('b_lower','res',0,255,nothing)
cv2.createTrackbar('g_lower','res',0,255,nothing)
cv2.createTrackbar('r_lower','res',0,255,nothing)

while (True):
    ret,frame=cap.read()
    frame=cv2.resize(frame,(620,480))
    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    if ret == False:
        break
    b_higher=cv2.getTrackbarPos('b_higher','res')
    g_higher=cv2.getTrackbarPos('g_higher','res')
    r_higher=cv2.getTrackbarPos('r_higher','res')
    b_lower=cv2.getTrackbarPos('b_lower','res')
    g_lower=cv2.getTrackbarPos('g_lower','res')
    r_lower=cv2.getTrackbarPos('r_lower','res')

    upper_blue=np.array([b_higher,g_higher,r_higher])  #100 67 65
    lower_blue=np.array([b_lower,g_lower,r_lower])   #112 255 255

    mask=cv2.inRange(frame,lower_blue,upper_blue)

    res=cv2.bitwise_and(frame,frame,mask=mask)
 #   ret, thresh = cv2.threshold(res, 1, 255, 0)
#    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    kernelM=np.ones((5,5),np.uint8)
    
    eroded=cv2.erode(mask,kernelM,iterations=1)
    erode=cv2.bitwise_and(frame,frame,mask=eroded)
    
    cv2.imshow('res',erode)    
    
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
cap.release()
print(upper_blue)
print(lower_blue)

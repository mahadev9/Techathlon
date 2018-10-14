import numpy as np
import cv2
z=0
while (z<116):
    
    im = cv2.imread('frame%d.jpg'%z)
    
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    canny=cv2.Canny(imgray,100,300)
    #ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    #im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #x=cv2.drawContours(im2, contours, -1, (0,255,0), 3)

    #print(im2,contours,hierarchy)
    #cv2.imshow("2",im)
    #cv2.waitKey()  
    #cv2.destroyAllWindows()
    #cv2.imshow("1",x)
    cv2.imwrite("zframe%d.jpg" % z,canny)
    z=z+1
    #cv2.waitKey()  
    #cv2.destroyAllWindows()

# Author imagean
# !/usr/bin/python
# -*- coding:utf-8
# opencv read image is BGR channel,and matplot read is RGB

import cv2
import numpy as np
img = cv2.imread('C:/Users/19845/Desktop/1234.jpg',0)

GrayImage= cv2.medianBlur(img,5)
ret,th1 = cv2.threshold(GrayImage,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(GrayImage,255,cv2.ADAPTIVE_THRESH_MEAN_C,
                    cv2.THRESH_BINARY,3,5)
th3 = cv2.adaptiveThreshold(GrayImage,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                    cv2.THRESH_BINARY,3,5)


kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(th2,kernel,iterations=1)
dilation = cv2.dilate(erosion,kernel,iterations=1)

imgray=cv2.Canny(erosion,30,100)

circles = cv2.HoughCircles(imgray,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=20,maxRadius=40)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
print(len(circles[0,:]))

cv2.imshow('detected circles',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

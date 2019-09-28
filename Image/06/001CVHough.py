# Author image
# !/usr/bin/python
# -*- coding:utf-8
# opencv read image is BGR channel,and matplot read is RGB

import cv2 as cv
import numpy as np

img = cv.imread('C:/Users/19845/Desktop/lena2.jpg',0)
#GaussianBlur
img = cv.GaussianBlur(img,(3,3),0)
#Canny Edges to Binary Image
edges =cv.Canny(img, 50, 150, apertureSize = 3) #Sobel算子的大小3

lines = cv.HoughLines(edges,1,np.pi/180,300)

result = img.copy()
minLineLength = 300
maxLineGap = 15
lines = cv.HoughLinesP(edges,1,np.pi/180,80,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv.line(edges,(x1,y1),(x2,y2),(255,255,255),2)
cv.imshow('result',edges)
cv.imshow('Original',img)
cv.waitKey(0)
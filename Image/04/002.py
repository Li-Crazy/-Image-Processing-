# Author imagean
#!/usr/bin/python
# -*- coding:utf-8
# A simple function hist

import cv2 as cv
import numpy as np
img = cv.imread("C:/Users/19845/Desktop/lena2.jpg")
rows,cols,channel = img.shape
cv.namedWindow('Original image')
cv.resizeWindow('Original image',640,480)
cv.imshow('Original image ',img)
# rotation image:getRotationMatrix2D function
# 1st is rotation point,2nd is rotation angle,3th is rotation rate
trans= cv.getRotationMatrix2D((cols/2,rows/2),-20,0.6)
#Affine transformation: 1st is orignal img ,2nd is rotation object ,3th is row/col
dst = cv.warpAffine(img,trans,(cols,rows))
cv.waitKey(0)
cv.imshow('Original image',dst)
cv.waitKey(0)
cv.destroyAllWindows()

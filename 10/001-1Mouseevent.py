# Author image
# !/usr/bin/python
# -*- coding:utf-8
# opencv read image is BGR channel,and matplot read is RGB

import cv2 as cv
import numpy as np
def on_mouse(event, x,y, flags , params):
    if event == cv.EVENT_LBUTTONDOWN:
        print('Point(',y,x ,')=',img[y,x])

img = cv.imread('C:/Users/19845/Desktop/01original.jpg',0)
cv.namedWindow('AAA',cv.WINDOW_FREERATIO)
cv.imshow('AAA',img)
print('img.shape=',img.shape)
cv.setMouseCallback('AAA', on_mouse)
cv.waitKey(0)

# Author image
# !/usr/python3/bin/python3.6
# -*- coding:utf-8
# opencv read image is BGR channel,and matplot read is RGB
import cv2 as cv
import numpy as np
def dis(f,H,W,channel):
    cv.namedWindow("imgs", 0)
    cv.resizeWindow("imgs",W*f.__len__(),H )
    cv.imshow('imgs',np.hstack(f))
    cv.waitKey()

if __name__ == '__main__':
    img = cv.imread('C:/Users/Zhang Bingjie/Pictures/KeNan1.jpg')
    (H,W,channel)=img.shape
    cv.imshow('Origianl',img)
    B,G,R =cv.split(img)
    files=[R,G,B]
    dis(files,H,W,channel)
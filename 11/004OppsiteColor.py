# Author image
# !/usr/python3/bin/python3.6
# -*- coding:utf-8
# opencv read image is BGR channel,and matplot read is RGB
import cv2 as cv
import numpy as np
def discolor(f,H,W):
    cv.namedWindow("Color imgs", 0)
    cv.resizeWindow("Color imgs",W*f.__len__(),H )
    cv.imshow('Color imgs',np.hstack(f))
    cv.waitKey()
def disgray(f,H,W):
    cv.namedWindow("Gray imgs", 0)
    cv.resizeWindow("Gray imgs",W*f.__len__(),H )
    cv.imshow('Gray imgs',np.hstack(f))
    cv.waitKey()

if __name__ == '__main__':
    img = cv.imread('C:/Users/19845/Desktop/123.jpg')
    (H,W,channel)=img.shape
    B,G,R =cv.split(img)
    nimg=cv.merge([255-B,255-G,255-R])
    files=[img,nimg]
    discolor(files,H,W)
    grayimg =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ngrayimg =255 -grayimg
    f = [grayimg,ngrayimg]
    disgray(f,H,W )

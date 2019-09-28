# Author image
# !/usr/python3/bin/python3.6
# -*- coding:utf-8
# opencv read image is BGR channel,and matplot read is RGB
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('C:/Users/19845/Desktop/123.jpg')
(H,W,channel)=img.shape
cv.imshow('Origianl',img)
B,G,R =cv.split(img)#分离多通道为单通道
cv.imshow("B",B)#b\g\r分别显示出单通道B/G/R
cv.imshow("G",cv.merge([B,G,R]))
cv.imshow("R",R)
files=cv.merge([R,G,B])
plt.subplot(121)
plt.imshow(img)
plt.title('B-G-R')
plt.subplot(122)
plt.imshow(files)
plt.title('R-G-B')
plt.show()

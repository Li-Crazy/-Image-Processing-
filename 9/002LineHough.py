# Author imagean
# !/usr/bin/python
# -*- coding:utf-8
# opencv read image is BGR channel,and matplot read is RGB

import cv2 as cv
import numpy as np

img = cv.imread('C:/Users/19845/Desktop/1234.jpg',0)
img = cv.GaussianBlur(img,(3,3),0)
edges = cv.Canny(img, 50, 150, apertureSize = 3)
#https://blog.csdn.net/longwinyang/article/details/52789260
lines = cv.HoughLines(edges,1,np.pi/180,118)
result = img.copy()
for line in lines[0]:
    rho = line[0]
    theta = line[1]
    print(rho)
    print(theta)
    if (theta < (np.pi / 4.0)) or (theta > (3.0 * np.pi / 4.0)):
        pt1 = (int(rho / np.cos(theta)), 0)
        pt2 = (int((rho - result.shape[0] * np.sin(theta)) / np.cos(theta)), result.shape[0])
        cv.line(result, pt1, pt2, (255))
    else:
        pt1 = (0, int(rho / np.sin(theta)))
        pt2 = (result.shape[1], int((rho - result.shape[1] * np.cos(theta)) / np.sin(theta)))
        cv.line(result, pt1, pt2, (255), 1)

cv.imshow('Canny', edges)
cv.imshow('Result', result)
cv.waitKey(0)
cv.destroyAllWindows()

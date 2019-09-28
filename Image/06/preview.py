# Author imagean
# !/usr/bin/python
# -*- coding:utf-8
# opencv read image is BGR channel,and matplot read is RGB
import cv2 as cv
import numpy as np
files = "C:/Users/19845/Desktop/lena2.jpg"
myimg = cv.imread(files,0)

param = 30
# 灰阶范围
grayscale = 256
w = myimg.shape[1]
h = myimg.shape[0]
newimg = np.zeros((h, w), np.uint8)
for x in range(0, h):
    for y in range(0, w, 2):
        r1 = np.random.random_sample()
        r2 = np.random.random_sample()
        z1 = param * np.cos(2 * np.pi * r2) * np.sqrt((-2) * np.log(r1))
        z2 = param * np.sin(2 * np.pi * r2) * np.sqrt((-2) * np.log(r1))
        fxy = int(myimg[x, y] + z1)
        fxy1 = int(myimg[x, y + 1] + z2)
        # f(x,y)
        if fxy < 0:
            fxy_val = 0
        elif fxy > grayscale - 1:
            fxy_val = grayscale - 1
        else:
            fxy_val = fxy
        # f(x,y+1)
        if fxy1 < 0:
            fxy1_val = 0
        elif fxy1 > grayscale - 1:
            fxy1_val = grayscale - 1
        else:
            fxy1_val = fxy1
        newimg[x, y] = fxy_val
        newimg[x, y + 1] = fxy1_val
cv.imshow('preview', newimg)
cv.waitKey()
cv.destroyAllWindows()
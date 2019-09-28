'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/4/28 11:18
@Software: PyCharm
@File    : gaosi.py
'''
import cv2 as cv
import numpy as np
import random
files = "C:/Users/19845/Desktop/01original.jpg"
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

def GaussianNoise(src,means,sigma,percentage):
    NoiseImg=src
    NoiseNum=int(percentage*src.shape[0]*src.shape[1])
    for i in range(NoiseNum):
        randX=random.randint(0,src.shape[0]-1)
        randY=random.randint(0,src.shape[1]-1)
        NoiseImg[randX, randY]=NoiseImg[randX,randY]+random.gauss(means,sigma)
        if  NoiseImg[randX, randY]< 0:
                 NoiseImg[randX, randY]=0
        elif NoiseImg[randX, randY]>255:
                 NoiseImg[randX, randY]=255
    return NoiseImg

img1 = GaussianNoise(myimg, 0.02, 10, 4)
cv.imshow('preview', newimg)
cv.imshow('img1',img1)
cv.waitKey()
cv.destroyAllWindows()

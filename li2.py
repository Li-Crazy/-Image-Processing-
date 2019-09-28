'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/6/23 10:28
@Software: PyCharm
@File    : li2.py
'''C:/Users/19845/Desktop/lena2.jpg
import cv2 as cv
import numpy as np
img=cv.imread("",1)
(H,W)=img.shape
for i in range(H):
    for j in range(W):
        Hist[img[i, j]] += 1
            for i in range(256):
                HistP[i] = Hist[i] / Pixelsum
                    for i in range(1, 256):
                        HistPSUM[i] = HistP[i] + HistPSUM[i - 1]
                            for i in range(256):
                                EqHist[i] = HistPSUM[i] * 255
                                    for i in range(H):
                                        for in range(W):
                                            [i, j] = EqHist[img[i, j]]
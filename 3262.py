# Author image
# !/usr/bin/python
# -*- coding:utf-8
# opencv read image is BGR channel,and matplot read is RGB

import cv2 as cv
import numpy as np
import time
from matplotlib import pyplot as plt

start = time.clock()
path  ="C:/Users/19845/Desktop/123.jpg"
img = cv.imread(path,0)
(H,W) =img.shape
files = [img]

def Robert(H,W,img):
    imgR = np.zeros((H,W),np.uint8)
    for i in range(0, H - 1):
        for j in range(0, W - 1):
            a00 = np.int16(img[i,j])
            a01 = np.int16(img[i,j+1])
            a10 = np.int16(img[i+1,j])
            a11 = np.int16(img[i+1,j+1])
            #u = np.sqrt((a00-a11)**2 + (a10-a01)**2)
            u = np.abs((a00-a11))+np.abs(a10-a01)
            if u>= 255:
                u = 255
            elif u<0:
                u = 0
            imgR[i,j] =np.uint8(u)
    return imgR

def Grad(H,W,img):
    imgG= np.zeros((H, W), np.uint8)
    for i in range(0, H - 1):
        for j in range(0, W - 1):
            a00 = np.int16(img[i, j])
            a01 = np.int16(img[i, j + 1])
            a10 = np.int16(img[i + 1, j])
            a11 = np.int16(img[i + 1, j + 1])
            u = np.sqrt(np.square(a10 - a00) + np.square(a01 - a00))
            if u >= 255:
                u = 255
            elif u < 0:
                u = 0
            imgG[i, j] = np.uint8(u)
    return imgG

if __name__ == '__main__':
    imgG = Grad(H,W,img)
    imgR = Robert(H,W,img)
    plt.subplot(131)
    plt.imshow(img,cmap='gray')
    plt.xticks([]), plt.yticks([])
    plt.title("Original")
    plt.subplot(132)
    plt.imshow(imgG, cmap='gray')
    plt.xticks([]), plt.yticks([])
    plt.title("Grad image")
    plt.subplot(133)
    plt.imshow(imgR, cmap='gray')
    plt.xticks([]), plt.yticks([])
    plt.title("Rebert image")
    end = time.clock()
    print(end - start)
    plt.show()



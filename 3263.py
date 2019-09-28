# Author image
# !/usr/bin/python
# -*- coding:utf-8
# opencv read image is BGR channel,and matplot read is RGB

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

path  ="C:/Users/19845/PycharmProjects/Project/cell.jpg"
img = cv.imread(path,0)
(H,W) =img.shape
files = [img]

def Prewitt(H,W,img):
    imgpX = np.zeros((H, W), np.uint8)
    imgpY = np.zeros((H, W), np.uint8)
    imgpXY = np.zeros((H, W), np.uint8)
    imgpS = np.zeros((H, W), np.uint8)
    for i in range(1, H - 1):
        for j in range(1, W - 1):
            a00 = img[i - 1, j - 1]
            a01 = img[i - 1, j]
            a02 = img[i - 1, j + 1]
            a10 = img[i, j - 1]
            a11 = img[i, j]
            a12 = img[i, j + 1]
            a20 = img[i + 1, j - 1]
            a21 = img[i + 1, j]
            a22 = img[i + 1, j + 1]
            ux = a20 * 1 + a10 * 1 + a00 * 1 + a02 * -1 + a12 * -1 + a22 * -1
            imgpX[i, j] = ux
            uy = a02 * 1 + a01 * 1 + a00 * 1 + a20 * -1 + a21 * -1 + a22 * -1
            imgpY[i, j] = uy
            imgpXY[i, j] = np.sqrt(ux * ux + uy * uy)
            imgpS[i, j] = np.abs(ux) + np.abs(uy)
    return imgpX, imgpY, imgpXY, imgpS

def Sobel(H,W,img):
    imgX = np.zeros((H,W),np.uint8)
    imgY = np.zeros((H,W),np.uint8)
    imgXandY = np.zeros((H,W),np.uint8)
    imgabS = np.zeros((H,W),np.uint8)
    for i in range(1,H-1) :
        for j in range (1,W-1):
            a00 = img[i-1, j-1]
            a01 = img[i-1, j]
            a02 = img[i-1, j+1]
            a10 = img[i,j-1]
            a11 = img[i,j]
            a12 = img[i, j+1]
            a20 = img[i+1, j-1]
            a21 = img[i+1, j]
            a22 = img[i+1, j+1]
            ux = a20 * 1 + a10 * 2 + a00 * 1  + a02 * -1 + a12 * -2 + a22 *-1
            imgX[i,j] = ux
            uy = a02 * 1 + a01 * 2 + a00 * 1+ a20 * -1 + a21 * -2 + a22 * -1
            imgY[i,j] = uy
            imgXandY[i,j] = np.sqrt(ux* ux+uy *uy)
            imgabS[i,j]  = np.abs(ux) + np.abs(uy)
    return imgX,imgY,imgXandY,imgabS



if __name__ == '__main__':

    (imgpX, imgpY, imgpXY, imgpS) = Prewitt(H,W,img)
    (imgX,imgY,imgXandY,imgabS) = Sobel(H, W, img)
    plt.subplot(221)
    plt.imshow(img,cmap='gray')
    plt.xticks([]), plt.yticks([])
    plt.title("Original")
    plt.subplot(222)
    plt.imshow(imgpS, cmap='gray')
    plt.xticks([]), plt.yticks([])
    plt.title("Prewitt image")
    plt.subplot(223)
    plt.imshow(imgXandY, cmap='gray')
    plt.xticks([]), plt.yticks([])
    plt.title("Sobel-1 image")
    plt.subplot(224)
    plt.imshow(imgabS, cmap='gray')
    plt.xticks([]), plt.yticks([])
    plt.title("Sobel-2 image")


    plt.show()

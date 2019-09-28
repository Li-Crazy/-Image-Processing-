# Author image
# !/usr/bin/python
# -*- coding:utf-8
# opencv read image is BGR channel,and matplot read is RGB

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
path  ="C:/Users/19845/Desktop/xibao.jpg"
img = cv.imread(path,0)
(H,W) = img.shape
print (H,W)

def dis(files,titles):
    lens = files.__len__()
    for i in range(lens):
        plt.subplot(1,3, i + 1)
        plt.imshow(files[i],cmap='gray')
        plt.xticks([]), plt.yticks([])
        plt.title(titles[i])
    plt.show()
def Laplace(H,W,img):
    #H1=np.mat([[0,1,0],        H2 =[[1,1,1]
    #           [1,-4,1],            [1,-8,1]
    #           [0,1,0]])            [1,1,1]]
    imgXYH1 = np.zeros((H,W),np.uint8)
    imgXYH2 = np.zeros((H,W),np.uint8)
    for i in range(1,H-2) :
        for j in range (1,W-2):
            a00 = np.int16(img[i - 1, j - 1])
            a01 = np.int16(img[i - 1, j])
            a02 = np.int16(img[i - 1, j + 1])
            a10 = np.int16(img[i, j - 1])
            a11 = np.int16(img[i, j])
            a12 = np.int16(img[i, j + 1])
            a20 = np.int16(img[i + 1, j - 1])
            a21 = np.int16(img[i + 1, j])
            a22 = np.int16(img[i + 1, j + 1])
            h1 = a10+a12+a01+a02-4*a11
            h2 = a10+a12+a01+a02+a00+a22+a21+a20 -8*a11
            if h1>255:
                h1=255
            elif h1<0:
                h1=0
            imgXYH1[i,j] = h1
            if h2 > 255:
                h2 = 255
            elif h2 < 0:
                h2 = 0
            imgXYH2[i,j] = h2
    files = [img, imgXYH1,imgXYH2]
    tiles = ['Original','H1 Template','H2 Template']
    dis(files,tiles)
if __name__ == '__main__':
    Laplace(H,W,img)

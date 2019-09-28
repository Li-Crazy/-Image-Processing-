'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/4/16 9:27
@Software: PyCharm
@File    : 高斯.py
'''
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
path = "C:/Users/19845/Desktop/"
originalfiles = "sandglass.png"
def gausspass(bimg,d):
    (rows, cols) = bimg.shape
    #butterworth low pass dis/d
    lmask = np.zeros(bimg.shape)
    #butterworth high pass d/dis
    hmask = np.ones(bimg.shape)
    for i in range(d):
        for j in range(d):
            dis1 = -(i**2+j**2)
            dis2 = 2*(d**2)
            dis = np.exp(dis1/dis2)
            lmask[rows//2-i:rows//2+i, cols//2-j:cols//2+j]=dis
            hmask[rows//2-i:rows//2+i,cols//2-j:cols//2+j]=1-dis
    f1=bimg*lmask
    ifs1 = np.fft.ifftshift(f1)
    lowf = np.abs(np.fft.ifft2(ifs1))
    lowf=(lowf- np.amin(lowf)) / (np.amax(lowf) - np.amin(lowf))

    f2 = bimg *hmask
    ifs2 = np.fft.ifftshift(f2)
    highf = np.abs(np.fft.ifft2(ifs2))
    highf = (highf - np.amin(highf)) / (np.amax(highf) - np.amin(highf))
    return lowf,highf

if __name__ == '__main__':
    img = cv.imread(path + originalfiles, 0)
    (H, W) = img.shape
    f1=np.fft.fft2(img)
    f1shift= np.fft.fftshift(f1)
    # Four angle imshow()
    f =np.log(np.abs(f1))
    # Central point imshow()
    fs=np.log(np.abs(f1shift))
    imga,imgb =gausspass(f1shift,30)
    plt.subplot(131),plt.imshow(img,cmap='gray'),plt.xticks([]),plt.yticks([]),plt.title('Original')
    plt.subplot(132), plt.imshow(imga, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('GaussLow Pass')
    plt.subplot(133), plt.imshow(imgb, cmap='gray'), plt.xticks([]), \
    plt.yticks([]), plt.title('GaussHigh Pass')
    plt.show()


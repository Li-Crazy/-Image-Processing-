'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/4/16 9:27
@Software: PyCharm
@File    : 巴特沃斯.py
'''
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
path = "C:/Users/19845/PycharmProjects/Project/"
originalfiles = "cell.jpg"

def butterpass(bimg,d,n):
    (rows, cols) = bimg.shape
    #butterworth low pass dis/d
    lmask = np.zeros(bimg.shape)
    #butterworth high pass d/dis
    hmask = np.ones(bimg.shape)
    for i in range(d):
        for j in range(d):
            dis=sqrt(i**2+j**2)
            lmask[rows//2-i:rows//2+i, cols//2-j:cols//2+j]=1/((1+(dis/d))**n)
    f1=bimg*lmask
    ifs1 = np.fft.ifftshift(f1)
    lowf = np.abs(np.fft.ifft2(ifs1))
    lowf=(lowf- np.amin(lowf)) / (np.amax(lowf) - np.amin(lowf))

    for i in range(d//2):
        for j in range(d//2):
            dis = sqrt(i**2+j**2)
            if dis>0:
                hmask[rows//2-i:rows//2+i,cols//2-j:cols//2+j]=1/((1+(d/dis))**n)
    f2 = bimg *hmask
    ifs2 = np.fft.ifftshift(f2)
    highf = np.abs(np.fft.ifft2(ifs2))
    highf = (highf - np.amin(highf)) / (np.amax(highf) - np.amin(highf))
    return lowf,highf
def bandpass(img,a,b,n):
    (rows, cols) = img.shape
    # butterworth low pass dis/d
    lmask = np.zeros(img.shape)
    # butterworth high pass d/dis
    hmask = np.ones(img.shape)
    for i in range(a):
        for j in range(a):
            dis = sqrt(i ** 2 + j ** 2)
            lmask[rows // 2 - i:rows// 2 + i, cols // 2 - j:cols // 2 + j] = 1 / ((1 + (dis /a)) ** n)
    for i in range(b):
        for j in range(b):
            dis = sqrt(i ** 2 + j ** 2)
            if dis > 0:
                hmask[rows //2 - i:rows //2 + i, cols// 2 - j:cols //2 + j] = 1 / ((1 + (b/dis)) ** n)
    f= img*(lmask * hmask)
    ifs = np.fft.ifftshift(f)
    bandf = np.abs(np.fft.ifft2(ifs))
    bandf = (bandf - np.amin(bandf)) / (np.amax(bandf) - np.amin(bandf))
    return bandf
def passfilter(img,a,b,n):
    (rows, cols) = img.shape
    # butterworth low pass dis/d
    lmask = np.ones(img.shape)
    # butterworth high pass d/dis
    hmask = np.zeros(img.shape)
    for i in range(a):
        for j in range(a):
            dis = sqrt(i ** 2 + j ** 2)
            lmask[rows //2 - i:rows //2 + i, cols //2 - j:cols // 2 + j] = 1 / ((1 + (dis / a)) ** n)
    for i in range(2*b):
        for j in range(2*b):
            dis = sqrt(i ** 2 + j ** 2)
            if dis > 0:
                hmask[rows //2 - i:rows //2 + i, cols //2 - j:cols// 2 + j] = 1 / ((1 + (b / dis)) ** n)
    f = img * (lmask * hmask)
    ifs = np.fft.ifftshift(f)
    passf = np.abs(np.fft.ifft2(ifs))
    passf = (passf - np.amin(passf)) / (np.amax(passf) - np.amin(passf))
    return bandf



if __name__ == '__main__':
    img = cv.imread(path + originalfiles, 0)
    (H, W) = img.shape
    f1=np.fft.fft2(img)
    f1shift= np.fft.fftshift(f1)
    # Four angle imshow()
    f =np.log(np.abs(f1))
    # Central point imshow()
    fs=np.log(np.abs(f1shift))
    imga,imgb =butterpass(f1shift,30,3)
    plt.subplot(231),plt.imshow(img,cmap='gray'),plt.xticks([]),plt.yticks([]),plt.title('Original')
    plt.subplot(232), plt.imshow(fs, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('After shift')
    plt.subplot(233), plt.imshow(imga, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('Butterworth Low')
    plt.subplot(234), plt.imshow(imgb, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('Butterworth High')
    bandf = bandpass(f1shift,30,15,3)
    plt.subplot(235), plt.imshow(bandf, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('Butterworth Band ')
    passf= passfilter(f1shift,30,15,3)
    plt.subplot(236), plt.imshow(passf, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('Butterworth Pass ')
    plt.show()

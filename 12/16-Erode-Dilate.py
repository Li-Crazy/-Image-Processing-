'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/5/21 9:38
@Software: PyCharm
@File    : 16-Erode-Dilate.py
'''
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
filename ='C:/Users/19845/Desktop/123.jpg'

def Lookformin(subimg):
    (row,col)=subimg.shape
    min = 0
    for i in range(row):
        for j in range(col):
            if subimg[i,j]>0:
                min =subimg[i,j]
                break
    for i in range(row):
        for j in range(col):
            if subimg[i, j] < min and subimg[i,j]>0:
                min = subimg[i, j]
    return min

def getDilate(img, kernel):
    (H,W) =img.shape
    dilate2 = np.zeros((H, W), np.uint8)
    print("img.shape(H,W)=", H, W)
    (row,col)=kernel.shape
    # 等于结构元素的子图像
    subimg = np.zeros((row, col), np.uint8)
    # 结构元素卷积运算原始图像
    print("kernel.shape(row,col)", row, col)
    for h in range(row//2, H-row//2):
        for w in range(col//2, W-col//2):
            #结构元素与对应点
            for i in range(-(row//2), row//2+1):
                for j in range(-(col//2), col//2+1):
                    subimg[row//2+i,col//2+j] = img[h+i,w+j]*kernel[row//2+i,col//2+j]
            smax = subimg.max()
            dilate2[h, w] = smax
    return dilate2

def getErode(img, kernel):
    (H,W) =img.shape
    erodeimg2 = np.zeros((H,W),np.uint8)
    print ("img.shape is (",H,W,")")
    (row,col)=kernel.shape
    print("kernel.shape(",row,col,")=\n", kernel)
    # 等于结构元素的子图像
    subimg = np.zeros((row, col), np.uint8)
    # 结构元素卷积运算原始图像
    for h in range(row//2, H-row//2):
        for w in range(col//2, W-col//2):
            #结构元素与对应点
            for i in range(-(row//2), row//2+1):
                for j in range(-(col//2), col//2+1):
                    subimg[row//2+i,col//2+j] = img[h+i,w+j]*kernel[row//2+i,col//2+j]

            smin = Lookformin(subimg)
            erodeimg2[h,w]=smin
    return erodeimg2

def Erode():
    image = cv.imread(filename)
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    print(image.shape)
    img = np.zeros(image.shape, np.uint8)
    kernel = np.array([[0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0]],
                      dtype=np.uint8)
    print(kernel)
    retval, image1 = cv.threshold(image, 127, 255, cv.THRESH_BINARY)#固定阈值二值化
    erodeimg1 = cv.erode(image1, kernel, iterations=1)
    erodeimg2 = getErode(image1, kernel)
    plt.figure(num='Basic Erode')
    plt.subplot(231), plt.imshow(image1, cmap='gray'), plt.title(
        "Original"), plt.xticks([]), plt.yticks([])
    plt.subplot(232), plt.imshow(erodeimg1, cmap='gray'), plt.title(
        "CV Erode"), plt.xticks([]), plt.yticks([])
    plt.subplot(233), plt.imshow(erodeimg2, cmap='gray'), plt.title(
        "My Erode"), plt.xticks([]), plt.yticks([])
    img[:] = (erodeimg2[:] + 1) / 128
    plt.subplot(234), plt.imshow(img, cmap='gray'), plt.title(
        "Binarization"), plt.xticks([]), plt.yticks([])
    plt.subplot(235), plt.imshow(image1 - erodeimg1, cmap='gray'), plt.title(
        "CV Edge"), plt.xticks([]), plt.yticks([])
    plt.subplot(236), plt.imshow(image1 - erodeimg2, cmap='gray'), plt.title(
        "My Edge"), plt.xticks([]), plt.yticks([])
    plt.show()

def Dilate():
    image = cv.imread(filename, 0)
    print(image.shape)
    img = np.zeros(image.shape, np.uint8)
    kernel = np.array(
        [[0, 0, 1, 0, 0], [0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0],
         [0, 0, 1, 0, 0]], dtype=np.uint8)
    print(kernel)
    retval, image1 = cv.threshold(image, 127, 255, cv.THRESH_BINARY)#固定阈值二值化
    dilate1 = cv.dilate(image1, kernel, iterations=1)
    dilate2 = getDilate(image1, kernel)
    plt.figure(num='Basic Dilate')
    plt.subplot(231), plt.imshow(image1, cmap='gray'), plt.title(
        "Original"), plt.xticks([]), plt.yticks([])
    plt.subplot(232), plt.imshow(dilate1, cmap='gray'), plt.title(
        "CV Dilate"), plt.xticks([]), plt.yticks([])
    plt.subplot(233), plt.imshow(dilate2, cmap='gray'), plt.title(
        "My Dilate"), plt.xticks([]), plt.yticks([])
    img[:] = (dilate1[:] + 1) / 128
    plt.subplot(234), plt.imshow(img, cmap='gray'), plt.title(
        "Binary Dilate"), plt.xticks([]), plt.yticks([])
    plt.subplot(235), plt.imshow(dilate1 - image1, cmap='gray'), plt.title(
        "CV edge "), plt.xticks([]), plt.yticks([])
    plt.subplot(236), plt.imshow(dilate2 - image1, cmap='gray'), plt.title(
        "My edge"), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == '__main__':
    Erode()
    Dilate()


'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/4/28 11:04
@Software: PyCharm
@File    : 6.5.py
'''

import cv2 as cv
import numpy as np

def drawHist(hist):
    img = np.zeros((256, 256), np.uint8)
    r = max(hist) / 255#数组中最大值除以255
    for i in range(0, 256):
        hist[i] = hist[i] / r
        cv.line(img, (i, 255), (i, 255 - hist[i]), 255)
    return img

def show_img(img):
    #使用opencv读取图像，直接返回numpy.ndarray 对象，通道顺序为BGR ，注意是BGR，通道值默认范围0-255。
    hist1 = cv.calcHist([img],  # 计算图像的直方图
                         [0],  # 使用的通道数
                         None,  # 没有使用mask，掩膜
                         [256],  # it is a 1D histogram，直方图大小，一般等于灰度级数
                         [0.0, 255.0])#横轴范围
    hist11 = hist1.cumsum()  # 累计直方图,求累计值不会改变原数组的值
    hist111 = hist11.reshape(hist1.shape)  # reshape也不会改变原数组的值
    # hist1是二维(ndim),hist11是一维

    a = drawHist(hist1)
    a1 = drawHist(hist111)
    cv.imshow("first", a)#均衡化前的直方图
    cv.imshow("second", a1)#均衡化前的累计直方图
    cv.imshow('img1',img)
    cv.waitKey()
    cv.destroyAllWindows()

if __name__ == '__main__':
    img = cv.imread("C:/Users/19845/Desktop/01original.jpg", 0)  # 0  灰度图模式
    show_img(img)
    img1 = cv.imread("C:/Users/19845/Desktop/02gaussian.jpg", 0)#0  灰度图模式
    img2 = cv.imread("C:/Users/19845/Desktop/03Poisson.jpg", 0)#0  灰度图模式
    img3 = cv.imread("C:/Users/19845/Desktop/04mutil.jpg", 0)#0  灰度图模式
    img4  = cv.imread("C:/Users/19845/Desktop/05salt.jpg", 0)#0  灰度图模式

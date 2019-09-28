#coding=utf-8
import cv2 as cv
import numpy as np

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

names = "C:/Users/19845/Desktop/123.jpg"
img = cv.imread(names, 0)
(H, W) = img.shape#图片维度
Newimg = np.zeros((H, W), np.uint8)#二维数组
Hist = np.zeros(256, np.int)  # Pixel sum一维均衡化前
EqHist = np.zeros(256, np.int)  # Equal Pixel均衡化后
HistP = np.zeros(256, np.float)  #像素概率
HistPSUM = np.zeros(256, np.float)  #像素概率和
Pixelsum = H * W


def display(files,l):
    cv.namedWindow("imgs", 0)
    cv.resizeWindow("imgs",l*H,W)
    cv.imshow('imgs', np.hstack(files))
    cv.waitKey(0)

# def pltshow(files):
#     plt.figure("hist")
#     arr = files.flatten()
#     n, bins, patches = plt.hist(arr, bins=256, normed=1, edgecolor='None', facecolor='red')
#     plt.show()

if __name__ == '__main__':
    for i in range(H):
        for j in range(W):
            # Every Gray Pixel sum
            Hist[img[i,j]]+=1#像素点出现的次数

    for i in range(256):
        HistP[i] =Hist[i]/Pixelsum#像素点出现的概率

    for i in range(1,256):
        HistPSUM[i] =HistP[i]+HistPSUM[i-1]#归一化

    for i in range(256):
        EqHist[i] =HistPSUM[i]*255#均衡化后灰度值

    for i in range(H):
        for j in range(W):
            # Set New pixels Gray
            Newimg[i,j]= EqHist[img[i,j]]

    plt.figure("hist")
    arr = Newimg.flatten()
    n, bins, patches = plt.hist(arr, bins=256, density=1, edgecolor='None', facecolor='red')
    plt.show()

    # files =[Newimg]
    imgs=[img,Newimg]
    lens =imgs.__len__()
    display(imgs,lens)
    # pltshow(files)



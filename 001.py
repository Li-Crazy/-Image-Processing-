# Author imagean
#!/usr/bin/python
# -*- coding:utf-8

import cv2 as cv
import numpy as np

img = cv.imread("C:/Users/19845/Desktop/1.jpg")#使用imread()函数读取图片
cv.imshow('Original image ',img)#载入的图片显示
cv.waitKey(0)#程序暂停，等待用户触发一个按键操作
#.INTER_LINEAR is default,means double liner interpolation
#.INTER_CUBIC is 4X4 neighbourhood interploration
#.INTER_AREA is turn small
imgtrans = cv.resize(img,None,fx=2,fy=2 ,interpolation=cv.INTER_CUBIC)#重新调整图像src（或它的ROI），使它精确匹配目标dst（或其ROI）
row,col,channel = img.shape
cv.imshow('zoom in fx=2,fy=2 iamge',imgtrans)

imgtrans = cv.resize(img,None,fx=2,fy=1 ,interpolation=cv.INTER_CUBIC)
cv.imshow("zoom in fx=2 ,fy=1",imgtrans)

imgtrans = cv.resize(img,None,fx=1,fy=2 ,interpolation=cv.INTER_CUBIC)
cv.imshow("zoom in fx=1 ,fy=2",imgtrans)

imgtrans = cv.resize(img,None,fx=0.8,fy=0.7 ,interpolation=cv.INTER_AREA)
cv.imshow("zoom in fx=0.8 ,fy=0.7",imgtrans)
#define trans Martix
#m =[1,0,tx]
#   [0,1,ty]
#is np.float32s
m = np.float32([[1,0,100],[0,1,50]])
# warpAfiine() is block tans function
# 1st is original image ,2nd is tansmatrix ,3th is output image size
dst = cv.warpAffine(img,m,(col,row))#对图像做仿射变换
cv.waitKey(0)
cv.imshow('Block trans iamge', dst)
cv.waitKey(0)
cv.destroyAllWindows()#销毁窗口

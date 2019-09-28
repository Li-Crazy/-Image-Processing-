# Author imagean
#!/usr/bin/python
# -*- coding:utf-8
# opencv read image is BGR channel,and matplot read is RGB
import cv2 as cv
import numpy as np
names = "C:/Users/19845/Desktop/lena2.jpg"
img = cv.imread(names, 0)
(H, W) = img.shape
Newimg = np.zeros((H, W), np.uint8)
Hist = np.zeros(256, np.int)  # Pixel sum
EqHist = np.zeros(256, np.int)  # Equal Pixel
HistP = np.zeros(256, np.float)  #
HistPSUM = np.zeros(256, np.float)  #
Pixelsum = H * W
def display(files,l):
    cv.namedWindow("imgs", 0)
    cv.resizeWindow("imgs",l*H,W)
    cv.imshow('imgs', np.hstack(files))
    cv.waitKey(0)
if __name__ == '__main__':
    for i in range(H):
        for j in range(W):
            # Every Gray Pixel sum
            Hist[img[i,j]]+=1
    for i in range(256):
        HistP[i] =Hist[i]/Pixelsum
    for i in range(1,256):
        HistPSUM[i] =HistP[i]+HistPSUM[i-1]
    for i in range(256):
        EqHist[i] =HistPSUM[i]*255
    for i in range(H):
        for j in range(W):
            # Set New pixels Gray
            Newimg[i,j]= EqHist[img[i,j]]
    imgs=[img,Newimg]
    lens =imgs.__len__()
    display(imgs,lens)

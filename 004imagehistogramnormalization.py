# Author imagean
# !/usr/bin/python
# -*- coding:utf-8
# opencv read image is BGR channel,and matplot read is RGB

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#  Display image histogram
def showHist(src):
    plt.hist(src.ravel(), 256, [0, 256])
    plt.xlim(0, 255)
    plt.xlabel('DN'), plt.ylabel('count')
    plt.title('histogram')
    plt.show()
    return

#  Statistical image Cumulative frequency
def cumFre(src):
    # get image size
    rows, cols = src.shape
    # get image histogram like (hist,bins = np.histogram(img.flatten(), 256, [0, 255]))
    hist = cv.calcHist([src], [0], None, [256], [0, 256])
    # get image hist_add is formula si
    cumHist = np.cumsum(hist)
    # Calculation of cumulative frequency of images
    cumf = cumHist / (rows*cols)
    return cumf

#  Histogram equalization
def histEq(src):
    rows, cols = src.shape
    hist = cv.calcHist([src], [0], None, [256], [0, 256])
    cumHist = np.cumsum(hist)
    LUT = np.zeros(256, np.float32)    #gary search sheet
    for i in range(256):
        LUT[i] = 255.0/(rows*cols) * cumHist[i]
    LUT = np.uint8(LUT + 0.5)
    dst = cv.LUT(src, LUT)             # search sheet
    return dst

# Histogram matching (image to be matched, reference image)
def histMatching(oriImage, refImage):
    oriCumHist = cumFre(oriImage)     #
    refCumHist = cumFre(refImage)     #
    lut = np.ones(256, dtype = np.uint8) * (256-1) #new search sheet
    start = 0
    for i in range(256-1):
        temp = (refCumHist[i+1] - refCumHist[i]) / 2.0 + refCumHist[i]
        for j in range(start, 256):
            if oriCumHist[j] <= temp:
                lut[j] = i
            else:
                start = j
                break

    dst = cv.LUT(oriImage, lut)
    return dst

if __name__ == '__main__':
    #  Using this image histogram as a normalization template
    refImg = cv.imread('C:/Users/19845/Desktop/123.jpg', 0)
    # This is  a original iamge
    oriImg = cv.imread('C:/Users/19845/Desktop/1.jpg',0)
    # def function to nomaliztion
    outImg = histMatching(oriImg, refImg)
    cv.imshow('original-Img is lena', oriImg)
    cv.imshow('refence- Img is house', refImg)
    cv.imshow('output lena Img', outImg)
    cv.waitKey(0)
    cv.destroyAllWindows()

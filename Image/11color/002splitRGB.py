# Author image
# !/usr/python3/bin/python3.6
# -*- coding:utf-8
# opencv read image is BGR channel,and matplot read is RGB
import cv2 as cv
from matplotlib import pyplot as plt

if __name__ == '__main__':
    img = cv.imread('/home/image/Pictures/sence.jpg')
    (H,W,channel)=img.shape
    cv.imshow('Origianl',img)
    B,G,R =cv.split(img)
    files=cv.merge([R,G,B])
    plt.subplot(121),plt.imshow(img),plt.title('B-G-R')
    plt.subplot(122),plt.imshow(files),plt.title('R-G-B')
    plt.show()

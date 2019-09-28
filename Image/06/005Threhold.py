# Author imagean
# !/usr/bin/python
# -*- coding:utf-8
# opencv read image is BGR channel,and matplot read is RGB
import cv2 as cv
from matplotlib import pyplot as plt
image = cv.imread('/home/image/Pictures/hough.png',0)
blurred = cv.GaussianBlur(image, (5, 5), 0)

#cv2.ADAPTIVE_THRESH_MEAN_C 平均值
thresh1 = cv.adaptiveThreshold(blurred, 255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 4)
#cv2.ADAPTIVE_THRESH_GAUSSIAN_C 高斯分布加权和
thresh2 = cv.adaptiveThreshold(blurred, 255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 15, 3)
plt.subplot(131), plt.imshow(blurred, "gray"),plt.title("Source Image"), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(thresh1, "gray"),plt.title("ADAPTIVE_THRESH_MEAN_C "), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(thresh2, "gray"),plt.title("ADAPTIVE_THRESH_GAUSSIAN_C "), plt.xticks([]), plt.yticks([])
plt.show()
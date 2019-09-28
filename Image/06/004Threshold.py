# Author imagean
# !/usr/bin/python
# -*- coding:utf-8
# opencv read image is BGR channel,and matplot read is RGB
import cv2 as cv
from matplotlib import pyplot as plt
image = cv.imread('C:/Users/19845/PycharmProjects/Project/cell.jpg',0)
blurred = cv.GaussianBlur(image, (5, 5), 0)
(T, thresh) = cv.threshold(blurred, 155, 255, cv.THRESH_BINARY)
(T, threshInv) = cv.threshold(blurred, 155, 255, cv.THRESH_BINARY_INV)
plt.subplot(131), plt.imshow(blurred, "gray"),plt.title("Source Image"), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(thresh, "gray"),plt.title("Thresh"), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(threshInv, "gray"),plt.title("threshInv"), plt.xticks([]), plt.yticks([])
plt.show()
# Author image
# !/usr/python3/bin/python3.6
# -*- coding:utf-8
# opencv read image is BGR channel,and matplot read is RGB

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
path  ="C:/Users/19845/PycharmProjects/Project/cell.jpg"
img = cv.imread(path,0)
(H,W) = img.shape
print (H,W)
def dis(files,titles):
    lens = files.__len__()
    rows = lens /2
    for i in range(lens):
        plt.subplot(2, rows, i + 1)
        plt.imshow(files[i],cmap='gray')
        plt.xticks([]), plt.yticks([])
        plt.title(titles[i])
    plt.show()

def laplacian(img):
    lap =  cv.Laplacian(img,cv.CV_8U)
    return lap

def soble(img):
    sx = cv.Sobel(img,cv.CV_8U,1,0)
    sy = cv.Sobel(img,cv.CV_8U,0,1)
    sx = np.uint8(np.absolute(sx))
    sy = np.uint8(np.absolute(sy))
    sc = cv.bitwise_or(sx,sy)
    return sx,sy,sc

def canny(img):
    cannyimg = cv.Canny(img,70,110)
    #边缘判别
    # 凡是边缘强度大于高阈值的一定是边缘点；凡是边缘强度小于低阈值的一定不是边缘点；
    # 如果边缘强度大于低阈值又小于高阈值，则看这个像素的邻接像素中有没有超过高阈值的边缘点，如果有，它就是边缘点，如果没有，它就不是边缘点。，
    cannyimg = np.uint8(np.absolute(cannyimg))
    return cannyimg

if __name__ == '__main__':
    lap = laplacian(img)
    sx,sy,sc = soble(img)
    cannimg = canny(img)
    files = [img,lap,sx,sy,sc,cannimg]
    titles=['Original','Laplacian','Sobel-x','Sobel-y','Sobel','Canny']
    dis(files,titles)




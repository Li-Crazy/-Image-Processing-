# Author imagean
#!/usr/bin/python
# -*- coding:utf-8
# opencv read image is BGR channel,and matplot read is RGB
import cv2 as cv
import numpy as np
import math
names = "C:/Users/19845/Desktop/1.jpg"
img = cv.imread(names,0)
(H,W)=img.shape
Mida = 80
Midb = 160
weighta = 180
weightb = 55
print(img[:])
def display(files):
    cv.namedWindow("imgs", 0)
    cv.resizeWindow("imgs",4*H,W)
    cv.imshow('imgs', np.hstack(files))

if __name__ == '__main__':
    img1 = np.zeros((H, W), np.uint8)
    img2 = np.zeros((H, W), np.uint8)
    img3 = np.zeros((H, W), np.uint8)
    for i in range(H):
        for j in range(W):
            if (img[i,j]>=Mida and img[i,j] <= Midb):
                img1[i,j] = weighta
            else:
                img1[i,j] = weightb
    for i in range(H):
        for j in range(W):
            if (img[i, j] >= Mida and img[i, j] <= Midb):
                img2[i, j] = weighta
            else:
                img2[i, j] = 0
    for i in range(H):
        for j in range(W):
            if (img[i, j] >= Mida and img[i, j] <=Midb):
                img3[i, j] = weighta

    files = [img, img1, img2,img3]
    display(files)
    cv.waitKey(0)
    cv.destroyAllWindows()


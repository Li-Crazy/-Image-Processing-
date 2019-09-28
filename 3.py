# Author imagean
# !/usr/bin/python
# -*- coding:utf-8
# opencv read image is BGR channel,and matplot read is RGB

import cv2 as cv
import numpy as np
img = cv.imread("C:/Users/19845/Desktop/1.jpg",0)
(H,W) =img.shape
print (H,W)

def display(title,imagenum,files):
    cv.namedWindow(title, 0)
    cv.resizeWindow(title,imagenum*H,W)
    cv.imshow(title, np.hstack(files))
    cv.waitKey(0)

def cur(img,imgnose):
    t1 = cv.getTickCount()

    curimg = np.zeros((H,W),np.uint8)
    template = np.mat([[1, 1, 1],
                      [1, 1, 1],
                      [1, 1, 1]])
    for i in range(0,H-1):
        for j in range(0,W-1):
            if (i ==0):
                if (j==0):
                    curimg[i,j] =(imgnose[i,j] * template[1,1] + imgnose[i,j + 1] * template[1, 2]
                    +imgnose[i + 1,j] * template[2, 1] + imgnose[i + 1, j + 1] * template[2, 2]) /4
                elif (j==W):
                    curimg[i,j] =(imgnose[i,j-1] * template[1, 0] + imgnose[i,j] * template[1,1]
                    +imgnose[i+1,j -1] * template[2, 0] + imgnose[i + 1,j] * template[2, 1])/4
                else:
                    curimg[i,j] =(imgnose[i,j-1] * template[1, 0] + imgnose[i,j] * template[1,1] + imgnose[i,j + 1] * template[1, 2]
                    + imgnose[i+1,j -1] * template[2, 0] + imgnose[i + 1,j] * template[2, 1] + imgnose[i + 1, j + 1] * template[2, 2]) / 6
            elif (i==H):
                if (j == 0):
                    curimg[i, j] = (imgnose[i-1,j] * template[0, 1] + imgnose[i-1, j + 1] * template[0, 2]
                    +imgnose[i,j] * template[1,1] + imgnose[i,j + 1] * template[1, 2])/4
                elif (j==W):
                    curimg[i, j] = (imgnose[i-1,j-1] * template[0, 0] + imgnose[i-1,j] * template[0, 1]
                    +imgnose[i,j-1] * template[1, 0] + imgnose[i,j] * template[1,1] )/4
                else:
                    curimg[i, j] =(imgnose[i-1,j-1] * template[0, 0] + imgnose[i-1,j] * template[0, 1] + imgnose[i-1, j + 1] * template[0, 2]
                    + imgnose[i,j-1] * template[1, 0] + imgnose[i,j] * template[1,1] + imgnose[i,j + 1] * template[1, 2])/6
            else:
                if (j == 0):
                    curimg[i, j] =(imgnose[i-1,j] * template[0, 1] + imgnose[i-1, j + 1] * template[0, 2]
                                   +imgnose[i,j] * template[1,1] + imgnose[i,j + 1] * template[1, 2]
                                   +imgnose[i + 1,j] * template[2, 1] + imgnose[i + 1, j + 1] * template[2, 2])/6

                elif (j == W):
                    curimg[i, j] =(imgnose[i-1,j-1] * template[0, 0] + imgnose[i-1,j] * template[0, 1]
                                   + imgnose[i,j-1] * template[1, 0] + imgnose[i,j] * template[1,1]
                                   +imgnose[i+1,j -1] * template[2, 0] + imgnose[i + 1,j] * template[2, 1])/6

                else:
                    curimg[i, j] = calculat(template,i,j)
    t2 = cv.getTickCount()
    print("template calc spend time is =", (t2 - t1) / cv.getTickFrequency(), 'second')

    display('original', 3, [img,imgnose,curimg])


def calculat(template,i,j):
    templ = (imgnose[i-1,j-1] * template[0, 0] + imgnose[i-1,j] * template[0, 1] + imgnose[i-1, j + 1] * template[0, 2]
             + imgnose[i,j-1] * template[1, 0] + imgnose[i,j] * template[1,1] + imgnose[i,j + 1] * template[1, 2]
             + imgnose[i+1,j -1] * template[2, 0] + imgnose[i + 1,j] * template[2, 1] + imgnose[i + 1, j + 1] * template[2, 2]) / 9
    return templ



if __name__ == '__main__':
    imgnose = np.zeros(img.shape,np.uint8)
    imgnose[:] = img[:]
    for i in range(1000):
        temp_x = np.random.randint(0, img.shape[0])
        temp_y = np.random.randint(0, img.shape[1])
        imgnose[temp_x][temp_y] = 255
    cur(img,imgnose)


# Author imagean
#!/usr/bin/python
# -*- coding:utf-8
# opencv read image is BGR channel,and matplot read is RGB
import cv2 as cv
import numpy as np
names = "C:/Users/19845/Desktop/1.jpg"
img = cv.imread(names,0)
(H,W)=img.shape
Uplimit =0
Downlimit =0
print( img[:])

def display(files):
    cv.namedWindow("imgs", 0)
    cv.resizeWindow("imgs",3*H,W)
    cv.imshow('imgs', np.hstack(files))


if __name__ == '__main__':
    img1_1 = np.zeros((H,W),np.uint8)
    img1_1[:] = img[:] * 1.2
    img0_8 = np.zeros((H,W),np.uint8)
    img0_8[:] = img[:] * 0.8
    files =[img,img1_1,img0_8]
    display(files)
    cv.waitKey(0)
    cv.destroyAllWindows()
#  Local enhancement
    img2_1 =np.zeros((H,W),np.uint8)
    for i in range(H):
        for j in range(W):
            if img[i,j] < 50:
                img2_1[i,j] = img[i,j]* 0.8
            elif img[i,j]> 180:
                x= img[i,j]*1.2
                if (x>256):
                    img2_1[i, j] =255
                else:
                    img2_1[i, j] =x
    img2_2 =np.zeros((H,W),np.uint8)
    for i in range(H):
        for j in range(W):
            if img[i, j] < 80:
                img2_2[i, j] = img[i, j] *1.2
            elif (img[i, j] > 160):
                img2_2[i,j] =img[i,j]* 0.8

    files =[img,img2_1,img2_2]
    display(files)
    cv.waitKey(0)
    cv.destroyAllWindows()

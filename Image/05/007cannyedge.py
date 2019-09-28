# Author image
# !/usr/bin/python
# -*- coding:utf-8
# opencv read image is BGR channel,and matplotlib read is RGB

import cv2 as cv
import numpy as np
import math

path ="C:/Users/19845/Desktop/xibao.jpg"
img = cv.imread(path)
(H,W,channel) =img.shape
print('image high is:',H,'pixel && image whith is:',W,'pixel')

def dis(title,total,files):
    cv.namedWindow(title, 0)
    cv.resizeWindow(title,total * H, W)
    cv.imshow(title,np.hstack(files))
    cv.waitKey(0)

def Gasuu(gaus,size,sigma):
    # This is Pi
    Pi = 4.0 * math.atan(1.0)
    center = size / 2
    sum =0.0
    for i in range(0,size):
        for j in range(0,size):
            # This is a gaussian Kernel
            deltax = (i- center)*(i- center)
            deltay = (j- center)*(j- center)
            sigma2 =2.0 *(sigma *sigma)
            temp1 = 1.0 /(Pi*sigma2)
            temp2 = math.exp(-((deltax+deltay))/sigma2)
            gaus[i,j]=temp1 * temp2
            sum =sum +gaus[i,j]
    for i in range(0, size):
        for j in range(0, size):
            gaus[i,j] =gaus[i,j] /sum
    print(gaus)

def Gasufilter(imgs,gaus,size):
    imggasu = np.zeros((H,W),np.uint8)
    for i in range(size/2,H-size/2):
        for j in range(size/2,W-size/2):
            sum =0.0
            for k in range(size):
                for l in range(size):
                    sum = sum + gaus[k,l]*imgs[i-k,j-l]
            imggasu[i,j] = np.uint8(sum)
    files =[imgs,imggasu]
    dis("Gaussian denoise image",files.__len__(),files)

def Sobel(imgs):
    #This is Sobel calclate process
    imgX = np.zeros((H, W), np.uint8)
    imgY = np.zeros((H, W), np.uint8)
    imgXY = np.zeros((H, W), np.uint8)
    imgO = np.zeros((H, W), np.uint8)
    point = np.zeros((H, W), np.float)

    for i in range(1, H - 1):
        for j in range(1, W - 1):
            a00 = imgs[i - 1, j - 1]
            a01 = imgs[i - 1, j]
            a02 = imgs[i - 1, j + 1]
            a10 = imgs[i, j - 1]
            a11 = imgs[i, j]
            a12 = imgs[i, j + 1]
            a20 = imgs[i + 1, j - 1]
            a21 = imgs[i + 1, j]
            a22 = imgs[i + 1, j + 1]
            ux = a20 * 1 + a10 * 2 + a00 * 1 + a02 * -1 + a12 * -2 + a22 * -1
            imgX[i, j] = ux
            uy = a02 * 1 + a01 * 2 + a00 * 1 + a20 * -1 + a21 * -2 + a22 * -1
            imgY[i, j] = uy
            if ux == 0:
                ux = 0.000000000001
            #calculate uy/ux angle
            point[i,j] = math.atan(uy/ux)*57.3
            # set angle from -pi/2 ~  pi/2 into  0 ~ pi
            point[i,j] = point[i,j] + 90
            imgO[i,j] = imgXY[i,j] = np.sqrt(ux * ux + uy * uy)
    #files = [imgs, imgX, imgY, imgXY]
    #dis("Sobel", files.__len__(), files)
    for i in range(1, H - 1):
        for j in range(1, W - 1):
            a00 = np.float(imgO[i - 1, j - 1])
            a01 = np.float(imgO[i - 1, j])
            a02 = np.float(imgO[i - 1, j + 1])
            a10 = np.float(imgO[i, j - 1])
            a11 = np.float(imgO[i, j])
            a12 = np.float(imgO[i, j + 1])
            a20 = np.float(imgO[i + 1, j - 1])
            a21 = np.float(imgO[i + 1, j])
            a22 = np.float(imgO[i + 1, j + 1])
            if (np.int32(point[i,j]) >0 & (np.int32(point[i,j])<=45)):
                if (a11 <= a12+(a02-a12)*math.tan(point[ i,j])) or (a11<=(a10+(a20-a10))*math.tan(point[i,j])):
                    imgO[i,j] = 0
            if(np.int32(point[i,j]) >45 & (np.int32(point[i,j])<=90)):
                if (a11 <= a01 + (a02 - a01) / math.tan(point[i, j])) or (a11 <= (a21 + (a20 - a21))/math.tan( point[i, j])):
                    imgO[i,j] = 0
            if (np.int32(point[i,j]) >90 & (np.int32(point[i,j])<=135)):
                if (a11 <= a01 + (a00 - a01) / math.tan(180-point[i, j])) or (a11 <= (a21 + (a22 - a21)) / math.tan(180-point[i, j])):
                    imgO[i, j] = 0
            if (np.int32(point[i,j]) >135 & (np.int32(point[i,j])<=180)):
                if (a11 <= a10 + (a00 - a10) * math.tan(180-point[i, j])) or (a11 <= (a12 + (a22 - a11)) * math.tan(180-point[i, j])):
                    imgO[i, j] = 0
    files = [imgs, imgX, imgY, imgXY, imgO]
    print("Calculate Sobel speed ",str((t2-t1)/cv.getTickFrequency()),"second")
    dis("Sobel", files.__len__(), files)
    lower =input("Input lower therholds")
    high = input("Input high therholds")
    doubleThrehold(imgO,lower,high)

def doubleThrehold(imgO,lower,high):
    for i in range(0,H-1):
        for j in range(0,W-1):
            if imgO[i,j] > high:
                imgO[i,j] =255
            if imgO[i,j] <lower:
                imgO[i,j] =0
    doublthreholdlink(imgO, lower, high)
    cv.imshow("Sobel +Canny's imgs",imgO)
    cv.waitKey(0)



def doublthreholdlink(imgs, lower,high):
    for i in range(1,H-1):
        for j in range(1,W-1):
            if ((imgs[i,j]>lower) and (imgs[i,j]<255)):
                if ((imgs[i-1,j-1]==255) or (imgs[i-1,j]==255) or (imgs[i-1,j+1]==255)
                    or (imgs[i,j-1]==255) or(imgs[i,j]==255) or (imgs[i,j+1]==255)
                    or(imgs[i+1,j-1]==255) or(imgs[i+1,j]==255) or (imgs[i+1,j+1]==255)):
                    imgs[i,j] = 255
                    #doublthreholdlink(imgs,lower,high)
                else:
                    imgs[i, j] = 0

if __name__ == '__main__':
    imgs = np.zeros((H, W), np.uint8)
    if channel == 3: #to 256 gray
        (b, g, r) = cv.split(img)
        imgs[:] = 0.114 * b + 0.587 * g + 0.299 * r
    else:
        imgs = img
    #gaussian template :kernelsize is templte size and sigma
    kernelsize = input("Gaus conver kernel size is ")
    kernelsigma = input("Gaus conver kernel sigma is ")
    s = (kernelsize, kernelsize)
    # gaussian template
    gaus = np.zeros(s)
    # calculate gaussian template
    Gasuu(gaus,kernelsize,kernelsigma)
    # Call Gasufilter
    Gasufilter(imgs, gaus, kernelsize)
    # Call sobel calculate
    Sobel(imgs)










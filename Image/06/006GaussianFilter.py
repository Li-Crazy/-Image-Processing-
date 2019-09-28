# Author image
# !/usr/bin/python
# -*- coding:utf-8
# opencv read image is BGR channel,and matplotlib read is RGB

import cv2 as cv
import numpy as np
import math
path ="C:/Users/19845/PycharmProjects/Project/cell.jpg"
img = cv.imread(path)
(H,W,channel) =img.shape
print ('image high is:',H,'pixel && image whith is:',W,'pixel',':channel=',channel)

def dis(title,total,files):
    cv.namedWindow(title, 0)
    cv.resizeWindow(title,total * H, W)
    cv.imshow(title,np.hstack(files))
    cv.waitKey(0)

def Gaussian(gaus,size,sigma):
    # This is Pi
    #Pi = 4.0 * math.atan(1.0)
    Pi = 3.14159
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
    print('sum = ',sum,'Gaussian templte =\n',gaus)
    return gaus

def LoG1(gaus,size,sigma):
    Pi = 4.0 * math.atan(1.0)
    center = size / 2
    sum = di = 0.0
    for i in range(0, size):
        for j in range(0, size):
            # This is a gaussian Kernel
            sigma2 = sigma**2
            xandy =-((i-center)**2 +(j-center)**2)/(2*sigma2)
            sigma4 = sigma2**2
            temp1 = -1.0 / (Pi * sigma4)
            temp2 = 1+ xandy
            temp3 = math.exp(xandy)
            gaus[i,j] = temp1*temp2*temp3
            sum = sum + gaus[i,j]
    di = sum /(float)(size**2)
    for i in range(0, size):
        for j in range(0, size):
            gaus[i,j] = -di+ gaus[i,j]
    print('Log float Template\n',gaus)
    return gaus

def Gasufilter(imgs,gaus,size):
    imggasu = np.zeros((H,W),np.uint8)
    for i in range(0,size//2):
        for j in range(0,size//2):
            imggasu[i,j] = imgs[i,j]
    for i in range(H-size//2,H-1):
        for j in range(W-size//2,W-1):
            imggasu[i, j] = imgs[i,j]
    for i in range(size//2,H-size//2):
        for j in range(size//2,W-size//2):
            sum =0.0
            for k in range(size):
                for l in range(size):
                    sum = sum + gaus[k,l]*imgs[i-k,j-l]
            imggasu[i,j] = np.uint8(sum)
    return imggasu

if __name__ == '__main__':
    imgs = np.zeros((H, W), np.uint8)
    if channel == 3:  # to 256 gray
        (b, g, r) = cv.split(img)
        imgs[:] = 0.114 * b + 0.587 * g + 0.299 * r
    else:
        imgs = img
    #for i in range(1000):
    #    temp_x = np.random.randint(0, img.shape[0])
    #    temp_y = np.random.randint(0, img.shape[1])
    #    imgs[temp_x][temp_y] = 255
    #gaussian template :kernelsize is templte size and sigma
    s1 = (5, 5)
    # gaussian template
    gaus1= np.zeros(s1)
    # calculate gaussian template
    gaus1 = Gaussian(gaus1,5,1.0)
    s2 = (5, 5)
    # gaussian template
    gaus2 = np.zeros(s2)
    # calculate gaussian template
    gaus2 = LoG1(gaus2,5,1.0)
    gaus3 = np.mat([[-2, -4, -4, -2, -2],
                    [-4, 0, 8, 0, -4],
                    [-4, 8, 24, 8, -4],
                    [-4, 0, 8, 0, -4],
                    [-2, -4, -4, -2, -2]])
    g1 = Gasufilter(imgs, gaus1, 3)
    g2 = Gasufilter(imgs, gaus2, 5)
    g3 = Gasufilter(imgs, gaus3, 5)
    files =[imgs,g1,g2,g3]
    dis("Gaussian denoise image", files.__len__(), files)




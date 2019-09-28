# Author image
# !/usr/bin/python
# -*- coding:utf-8
# opencv read image is BGR channel,and matplotlib read is RGB

import cv2 as cv
import numpy as np
import math
# Pi = 4.0 * math.atan(1.0)
Pi = 3.14159
def Gaussian(size,sigma):
    gaus =np.zeros((size,size))
    center = size // 2
    sum =0.0
    for i in range(0,size):
        for j in range(0,size):
            # This is a gaussian Kernel
            deltax = (i- center)**2
            deltay = (j- center)**2
            sigma2 =2.0 *(sigma *sigma)
            temp1 = 1.0 /(Pi*sigma2)
            temp2 = math.exp(-((deltax+deltay))/sigma2)
            gaus[i,j]=temp1 * temp2
            sum =sum +gaus[i,j]
    for i in range(0, size):
        for j in range(0, size):
            gaus[i,j] =gaus[i,j] /sum
    print('sum = ',sum,'\nGaussian templte =\n',gaus)
    return gaus


def LOG1(size,sigma):
    gaus =np.zeros((size,size))
    center = size // 2
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

if __name__ == '__main__':
    #for i in range(1000):
    #    temp_x = np.random.randint(0, img.shape[0])
    #    temp_y = np.random.randint(0, img.shape[1])
    #    imgs[temp_x][temp_y] = 255
    #gaussian template :kernelsize is templte size and sigma
    #s1 = (5, 5)
    # gaussian template
    #gaus1= np.zeros(s1)
    # calculate gaussian template
    gaus1 = Gaussian(5,1.0)
    s2= (5, 5)
    # gaussian template
    gaus2 = np.zeros(s2)
    # calculate gaussian template
    gaus2 = LOG1(5,1.0)
    gaus3 = np.mat([[-2, -4, -4, -2, -2],
                    [-4,  0,  8,  0, -4],
                    [-4,  8,  24, 8, -4],
                    [-4,  0,  8,  0, -4],
                    [-2, -4, -4, -2, -2]])





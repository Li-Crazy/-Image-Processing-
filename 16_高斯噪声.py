import cv2 as cv
from numpy import shape
import random
import math
import numpy as np
from matplotlib import pyplot as plt

#加高斯噪声
def GaussianNoise(src,means,sigma,percetage):
    NoiseImg=src
    NoiseNum=int(percetage*src.shape[0]*src.shape[1])
    for i in range(NoiseNum):
        randX=random.randint(0,src.shape[0]-1)
        randY=random.randint(0,src.shape[1]-1)
        NoiseImg[randX, randY]=NoiseImg[randX,randY]+random.gauss(means,sigma)
        if  NoiseImg[randX, randY]< 0:
                 NoiseImg[randX, randY]=0
        elif NoiseImg[randX, randY]>255:
                 NoiseImg[randX, randY]=255
    return NoiseImg

#图片输出
def display(title,total,files):
    cv.namedWindow(title, 0)
    cv.resizeWindow(title,total * H, W)
    cv.imshow(title,np.hstack(files))
    cv.waitKey(0)

#高斯滤波
def Gasuu(gaus,size,sigma):
    # This is Pi
    Pi = 4.0 * math.atan(1.0)
    center = int(size / 2)
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
    return gaus

def Gasufilter(imgs,gaus,size):
    imggasu = np.zeros((H,W),np.uint8)
    for i in range(int(size/2),int(H-size/2)):
        for j in range(int(size/2),int(H-size/2)):
            sum =0.0
            for k in range(size):
                for l in range(size):
                    sum = sum + gaus[k,l]*imgs[i-k,j-l]
            imggasu[i,j] = np.uint8(sum)
    files =[imgs,imggasu]
    display("Gaussian denoise image",files.__len__(),files)
    return imggasu

#拉普拉斯锐化
def dis(files,titles):
    lens = files.__len__()
    for i in range(lens):
        plt.subplot(1,5, i + 1)
        plt.imshow(files[i],cmap='gray')
        plt.xticks([]), plt.yticks([])
        plt.title(titles[i])
    plt.show()
def Synthetic(H,W,img):
    # H6=np.mat([[0,-1,0],        H9 =[[-1,-1,-1]
    #           [-1,5,-1],            [-1, 9 ,-1]
    #           [0,-1,0]])            [-1,-1,-1]]
    imgXYH1 = np.zeros((H, W), np.uint8)
    imgXYH2 = np.zeros((H, W), np.uint8)
    imgXYH3 = np.zeros((H, W), np.uint8)
    imgXYH4 = np.zeros((H, W), np.uint8)
    for i in range(1, H - 2):
        for j in range(1, W - 2):
            a00 = np.int16(img[i - 1, j - 1])
            a01 = np.int16(img[i - 1, j])
            a02 = np.int16(img[i - 1, j + 1])
            a10 = np.int16(img[i, j - 1])
            a11 = np.int16(img[i, j])
            a12 = np.int16(img[i, j + 1])
            a20 = np.int16(img[i + 1, j - 1])
            a21 = np.int16(img[i + 1, j])
            a22 = np.int16(img[i + 1, j + 1])
            h1 = -a10 - a12 - a01 - a02 +5* a11
            h2 = -a10 - a12 - a01 - a02 - a00 - a22 - a21 - a20 + 9 * a11
            h3 = a10 + a12 + a01 + a02 - 5 * a11
            h4 = a10 + a12 + a01 + a02 + a00 + a22 + a21 + a20 - 9 * a11
            if h1 > 255:
                h1 = 255
            elif h1 < 0:
                h1 = 0
            imgXYH1[i, j] = h1
            if h2 > 255:
                h2 = 255
            elif h2 < 0:
                h2 = 0
            imgXYH2[i, j] = h2
            if h3 > 255:
                h3 = 255
            elif h3 < 0:
                h3 = 0
            imgXYH3[i, j] = h3
            if h4 > 255:
                h4 = 255
            elif h4 < 0:
                h4 = 0
            imgXYH4[i, j] = h4
    files = [img, imgXYH1, imgXYH2,imgXYH3, imgXYH4]
    tiles = ['Original', 'H6 Template', 'H7 Template','H8 Template', 'H9 Template']
    dis(files, tiles)

if __name__ == '__main__':
    img = cv.imread('C:/Users/19845/Desktop/original.jpg', 0)
    img1 = GaussianNoise(img, 2, 4, 0.8)
    cv.imshow('PepperandSalt', img1)
    cv.waitKey(0)
    (H, W) = img1.shape
    print('image high is:', H, 'pixel && image whith is:', W, 'pixel')
    imgs = np.zeros((H, W), np.uint8)
    imgs = img
    kernelsize = int(input("Gaus conver kernel size is "))
    kernelsigma = int(input("Gaus conver kernel sigma is "))
    s = (kernelsize, kernelsize)
    print(s)
    gaus = np.zeros(s)
    Gasuu(gaus, kernelsize, kernelsigma)
    Gasufilter = Gasufilter(imgs, gaus, kernelsize)
    Synthetic(H,W,Gasufilter)


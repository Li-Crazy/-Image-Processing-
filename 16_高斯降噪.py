'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/4/30 8:03
@Software: PyCharm
@File    : 高斯降噪.py
'''
import cv2 as cv
import numpy as np
import math
import matplotlib.pyplot as plt

path = "C:/Users/19845/Desktop/01original.jpg"
img = cv.imread(path,0)
img1 = cv.imread(path)
(H, W, channel) = img1.shape

#加高斯噪声
def GaussianNoise(img):
    param = 30
    # 灰阶范围
    grayscale = 256
    w = img.shape[1]
    h = img.shape[0]
    newimg = np.zeros((h, w), np.uint8)

    for x in range(0, h):
        for y in range(0, w, 2):
            r1 = np.random.random_sample()
            r2 = np.random.random_sample()
            z1 = param * np.cos(2 * np.pi * r2) * np.sqrt((-2) * np.log(r1))
            z2 = param * np.sin(2 * np.pi * r2) * np.sqrt((-2) * np.log(r1))

            fxy = int(img[x, y] + z1)
            fxy1 = int(img[x, y + 1] + z2)
            # f(x,y)
            if fxy < 0:
                fxy_val = 0
            elif fxy > grayscale - 1:
                fxy_val = grayscale - 1
            else:
                fxy_val = fxy
            # f(x,y+1)
            if fxy1 < 0:
                fxy1_val = 0
            elif fxy1 > grayscale - 1:
                fxy1_val = grayscale - 1
            else:
                fxy1_val = fxy1
            newimg[x, y] = fxy_val
            newimg[x, y + 1] = fxy1_val

    return newimg

def display(title,img):
    cv.imshow(title,img)
    cv.waitKey()
    cv.destroyAllWindows()

#频率域高斯带通滤波
def gausspass(bimg,d):
    (rows, cols) = bimg.shape
    #butterworth low pass dis/d
    lmask = np.zeros(bimg.shape)
    #butterworth high pass d/dis
    hmask = np.ones(bimg.shape)
    for i in range(d):
        for j in range(d):
            dis1 = -(i**2+j**2)
            dis2 = 2*(d**2)
            dis = np.exp(dis1/dis2)
            lmask[rows//2-i:rows//2+i, cols//2-j:cols//2+j]=dis
            hmask[rows//2-i:rows//2+i,cols//2-j:cols//2+j]=1-dis
    f1=bimg*lmask
    ifs1 = np.fft.ifftshift(f1)
    lowf = np.abs(np.fft.ifft2(ifs1))
    lowf=(lowf- np.amin(lowf)) / (np.amax(lowf) - np.amin(lowf))

    return lowf

def fft(img):
    f=np.fft.fft2(img)
    f1shift= np.fft.fftshift(f)#中心到原点
    # Four angle imshow()
    f1 =np.log(np.abs(f))#中心点对应赋值
    # Central point imshow()
    fs1=np.log(np.abs(f1shift))
    return [f1shift,f1,fs1]

#带通滤波
def passfilter(filterf):
    (rows, cols) = filterf.shape
    # np.ones() is set all uint of 2-Array value  is 1
    highmask = np.ones((rows,cols), np.uint8)
    highmask[rows//2-40:rows//2+40,cols//2-40:cols//2+40] = 0
# highpass filter is Convolution1_pulsenoise
    f1 = filterf*highmask
    ifs1 = np.fft.ifftshift(f1)
    highf = np.log(np.abs(np.fft.ifft2(ifs1)))
    # np.zeros() is set all uint of 2-Array value  is 0
    lowmask = np.zeros((rows, cols), np.uint8)
    lowmask[rows//2-40:rows//2+40,cols//2-40:cols//2+40] = 1
# lowpass filter is Convolution
    f2 = filterf * lowmask
    ifs2 = np.fft.ifftshift(f2)
    lowf = np.log(np.abs(np.fft.ifft2(ifs2)))
# pass filter
    mask1 = np.ones(filterf.shape, np.uint8)
    mask1[rows // 2 - 40:rows // 2 + 40, cols // 2 - 40:cols // 2 +40] = 0
    mask2 = np.zeros(filterf.shape, np.uint8)
    mask2[rows // 2 - 80:rows // 2 + 80, cols // 2 - 80:cols // 2 + 80] = 1
    mask = mask1 * mask2
    f3 = filterf * mask
    ifs3 = np.fft.ifftshift(f3)
    passf = np.log(np.abs(np.fft.ifft2(ifs3)))

    files=[lowf,highf,passf]
    return files

def displt(files,len,titles):
    for i in range(len):
        plt.subplot(2,len/2,i+1)
        plt.imshow(files[i],cmap='gray')
        plt.xticks([]),plt.yticks([])
        plt.title(titles[i])
    plt.show()

#原图
def original(img):
    imgfft = fft(img)
    allimg = passfilter(imgfft[0])
    allimg.insert(0, img)
    len1 = allimg.__len__()
    ti = ['Original', 'Low pass', 'High pass', 'Pass']
    displt(allimg, len1, ti)

    f1 = np.fft.fft2(img)
    f1shift = np.fft.fftshift(f1)
    # Four angle imshow()
    f = np.log(np.abs(f1))
    # Central point imshow()
    fs = np.log(np.abs(f1shift))
    imga = gausspass(f1shift, 30)
    plt.subplot(121), plt.imshow(img, cmap='gray'), plt.xticks([]), plt.yticks(
        []), plt.title('Original')
    plt.subplot(122), plt.imshow(imga, cmap='gray'), plt.xticks([]), plt.yticks(
        []), plt.title('GaussLow Pass')
    plt.show()

#加了高斯噪声
def gaussian(img):
    imgfft = fft(img)
    allimg = passfilter(imgfft[0])
    allimg.insert(0, img)
    len1 = allimg.__len__()
    ti = ['Gaussian', 'Low pass', 'High pass', 'Pass']
    displt(allimg, len1, ti)

    f1 = np.fft.fft2(img)
    f1shift = np.fft.fftshift(f1)
    # Four angle imshow()
    f = np.log(np.abs(f1))
    # Central point imshow()
    fs = np.log(np.abs(f1shift))
    imga = gausspass(f1shift, 30)
    plt.subplot(121), plt.imshow(img, cmap='gray'), plt.xticks([]), plt.yticks(
        []), plt.title('Gaussian')
    plt.subplot(122), plt.imshow(imga, cmap='gray'), plt.xticks([]), plt.yticks(
        []), plt.title('GaussLow Pass')
    plt.show()

def dis(title,total,files):
    cv.namedWindow(title, 0)
    cv.resizeWindow(title,total * H, W)
    cv.imshow(title,np.hstack(files))
    cv.waitKey(0)

#高斯矩阵
def gaus(channel):
    imgs = np.zeros((H, W), np.uint8)
    if channel == 3:  # to 256 gray
        (b, g, r) = cv.split(img1)
        imgs[:] = 0.114 * b + 0.587 * g + 0.299 * r
    else:
        imgs = img1
    # gaussian template :kernelsize is templte size and sigma
    kernelsize = 5
    kernelsigma = 1
    s = (kernelsize, kernelsize)
    # gaussian template
    print(s)
    gaus = np.zeros(s)
    # calculate gaussian template
    ga = Gasuu(gaus, kernelsize, kernelsigma)
    # Call Gasufilter
    return ga,kernelsize
    # Call sobel calculate

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

#空间域高斯滤波
def Gasufilter(imgs,gaus,size):
    imggasu = np.zeros((H,W),np.uint8)
    for i in range(int(size/2),int(H-size/2)):
        for j in range(int(size/2),int(H-size/2)):
            sum =0.0
            for k in range(size):
                for l in range(size):
                    sum = sum + gaus[k,l]*imgs[i-k,j-l]
            imggasu[i,j] = np.uint8(sum)
    files = [imgs, imggasu]
    dis("Gaussian denoise image", files.__len__(), files)

if __name__ == '__main__':

    display('Original',img)
    original(img)
    ga,kernelsize = gaus(channel)
    Gasufilter(img, ga, kernelsize)

    newimg = GaussianNoise(img)
    display('GaussianNoise',newimg)
    gaussian(newimg)
    ga, kernelsize = gaus(channel)
    Gasufilter(newimg, ga, kernelsize)





'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/4/18 10:01
@Software: PyCharm
@File    : 16.py
'''
import cv2 as cv
import random
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("C:/Users/19845/Desktop/1234.jpg", 0)
(H, W) = img.shape

def display(title,imagenum,files):
    cv.namedWindow(title, 0)
    cv.resizeWindow(title,imagenum*H,W)
    cv.imshow(title, np.hstack(files))
    cv.waitKey(0)

def displt(files,len,titles):
    for i in range(len):
        plt.subplot(2,len/2,i+1)
        plt.imshow(files[i],cmap='gray')
        plt.xticks([]),plt.yticks([])
        plt.title(titles[i])
    plt.show()

#加椒盐噪声
def PepperandSalt(src,percetage):
    NoiseImg=src
    NoiseNum=int(percetage*src.shape[0]*src.shape[1])
    for i in range(NoiseNum):
        randX=np.random.random_integers(0,src.shape[0]-1)
        randY=np.random.random_integers(0,src.shape[1]-1)
        if np.random.random_integers(0,1)<=0.5:
            NoiseImg[randX,randY]=0
        else:
            NoiseImg[randX,randY]=255
    return NoiseImg

#加高斯噪声
def GaussianNoise(src,means,sigma,percentage):
    NoiseImg=src
    NoiseNum=int(percentage*src.shape[0]*src.shape[1])
    for i in range(NoiseNum):
        randX=random.randint(0,src.shape[0]-1)
        randY=random.randint(0,src.shape[1]-1)
        NoiseImg[randX, randY]=NoiseImg[randX,randY]+random.gauss(means,sigma)
        if  NoiseImg[randX, randY]< 0:
                 NoiseImg[randX, randY]=0
        elif NoiseImg[randX, randY]>255:
                 NoiseImg[randX, randY]=255
    return NoiseImg

#中值滤波
def cross5x5(imgnose):
    t1 = cv.getTickCount()
    curimg = np.zeros((H,W),np.uint8)
    for i in range(2,H-3):
        for j in range(2,W-3):
            t00 = imgnose[i-2,j-2]
            t01 = imgnose[i-2,j-1]
            t02 = imgnose[i-2,j]
            t03 = imgnose[i-2,j+1]
            t04 = imgnose[i-2,j+2]
            t10 = imgnose[i-1, j - 2]
            t11 = imgnose[i-1, j - 1]
            t12 = imgnose[i-1, j]
            t13 = imgnose[i-1, j + 1]
            t14 = imgnose[i-1, j + 2]
            t20 = imgnose[i , j - 2]
            t21 = imgnose[i , j - 1]
            t22 = imgnose[i , j]
            t23 = imgnose[i , j + 1]
            t24 = imgnose[i , j + 2]
            t30 = imgnose[i+1, j - 2]
            t31 = imgnose[i+1, j - 1]
            t32 = imgnose[i+1, j]
            t33 = imgnose[i+1, j + 1]
            t34 = imgnose[i+1, j + 2]
            t40 = imgnose[i+2, j - 2]
            t41 = imgnose[i+2, j - 1]
            t42 = imgnose[i+2, j]
            t43 = imgnose[i+2, j + 1]
            t44 = imgnose[i+2, j + 2]
            templ =[t00,t01,t02,t03,t04,t10,t11,t12,t13,t14,t20,t21,t22,t23,t24,t30,t31,t32,t33,t34,t40,t41,t42,t43,t44]
            templ.sort()
            curimg[i,j]=templ[12]
    t2 = cv.getTickCount()
    print("Time1:",str((t2-t1)/cv.getTickFrequency()))
    return curimg

def fft(img):
    f=np.fft.fft2(img)
    f1shift= np.fft.fftshift(f)#中心到原点
    # Four angle imshow()
    f1 =np.log(np.abs(f))#中心点对应赋值
    # Central point imshow()
    fs1=np.log(np.abs(f1shift))
    return [f1shift,f1,fs1]

def display_GaussianNoise():
    def passfilter(filterf):
        t1 = cv.getTickCount()
        (rows, cols) = filterf.shape
        # np.ones() is set all uint of 2-Array value  is 1
        highmask = np.ones((rows, cols), np.uint8)
        highmask[rows // 2 - 40:rows // 2 + 40,
        cols // 2 - 40:cols // 2 + 40] = 0
        # highpass filter is Convolution1_pulsenoise
        f1 = filterf * highmask
        ifs1 = np.fft.ifftshift(f1)
        highf = np.log(np.abs(np.fft.ifft2(ifs1)))
        # np.zeros() is set all uint of 2-Array value  is 0
        lowmask = np.zeros((rows, cols), np.uint8)
        lowmask[rows // 2 - 40:rows // 2 + 40,
        cols // 2 - 40:cols // 2 + 40] = 1
        # lowpass filter is Convolution
        f2 = filterf * lowmask
        ifs2 = np.fft.ifftshift(f2)
        lowf = np.log(np.abs(np.fft.ifft2(ifs2)))
        # pass filter
        mask1 = np.ones(filterf.shape, np.uint8)
        mask1[rows // 2 - 20:rows // 2 + 20, cols // 2 - 20:cols // 2 + 20] = 0
        mask2 = np.zeros(filterf.shape, np.uint8)
        mask2[rows // 2 - 80:rows // 2 + 80, cols // 2 - 80:cols // 2 + 80] = 1
        mask = mask1 * mask2
        f3 = filterf * mask
        ifs3 = np.fft.ifftshift(f3)
        passf = np.log(np.abs(np.fft.ifft2(ifs3)))

        files = [lowf, highf, passf]
        t2 = cv.getTickCount()
        print("Time2:", str((t2 - t1) / cv.getTickFrequency()))
        return files

    img1 = GaussianNoise(img, 2, 4, 0.8)
    display("GaussianNoise", 1, [img1])
    curimg1 = cross5x5(img1)
    display('Medianfilter', 1, [curimg1])
    imgfft = fft(img1)
    allimg = passfilter(imgfft[0])
    allimg.insert(0, img1)
    len1 = allimg.__len__()
    ti = ['Original', 'Low pass', 'High pass', 'Pass']
    displt(allimg, len1, ti)

def display_PepperandSalt():
    def passfilter(filterf):
        t1 = cv.getTickCount()
        (rows, cols) = filterf.shape
        # np.ones() is set all uint of 2-Array value  is 1
        highmask = np.ones((rows, cols), np.uint8)
        highmask[rows // 2 - 20:rows // 2 + 20,
        cols // 2 - 20:cols // 2 + 20] = 0
        # highpass filter is Convolution1_pulsenoise
        f1 = filterf * highmask
        ifs1 = np.fft.ifftshift(f1)
        highf = np.log(np.abs(np.fft.ifft2(ifs1)))
        # np.zeros() is set all uint of 2-Array value  is 0
        lowmask = np.zeros((rows, cols), np.uint8)
        lowmask[rows // 2 - 40:rows // 2 + 40,
        cols // 2 - 40:cols // 2 + 40] = 1
        # lowpass filter is Convolution
        f2 = filterf * lowmask
        ifs2 = np.fft.ifftshift(f2)
        lowf = np.log(np.abs(np.fft.ifft2(ifs2)))
        # pass filter
        mask1 = np.ones(filterf.shape, np.uint8)
        mask1[rows // 2 - 10:rows // 2 + 10, cols // 2 - 10:cols // 2 + 10] = 0
        mask2 = np.zeros(filterf.shape, np.uint8)
        mask2[rows // 2 - 180:rows // 2 + 180,
        cols // 2 - 180:cols // 2 + 180] = 1
        mask = mask1 * mask2
        f3 = filterf * mask
        ifs3 = np.fft.ifftshift(f3)
        passf = np.log(np.abs(np.fft.ifft2(ifs3)))

        files = [lowf, highf, passf]
        t2 = cv.getTickCount()
        print("Time2:", str((t2 - t1) / cv.getTickFrequency()))
        return files

    img2 = PepperandSalt(img, 0.1)
    display("PepperandSalt", 1, [img2])
    curimg2 = cross5x5(img2)
    display('Medianfilter', 1, [curimg2])
    imgfft = fft(img2)
    allimg = passfilter(imgfft[0])
    allimg.insert(0, img2)
    len1 = allimg.__len__()
    ti = ['Original', 'Low pass', 'High pass', 'Pass']
    displt(allimg, len1, ti)

if __name__ == '__main__':
    display_GaussianNoise()
    display_PepperandSalt()




import cv2 as cv
import random
import numpy as np
from matplotlib import pyplot as plt

def display(title,imagenum,files):
    cv.namedWindow(title, 0)
    cv.resizeWindow(title,imagenum*H,W)
    cv.imshow(title, np.hstack(files))
    cv.waitKey(0)
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

def curcross(imgnose):
    curimg = np.zeros((H,W),np.uint8)
    for i in range(2,H-3):
        for j in range(2,W-3):
            t00 = imgnose[i, j - 2]
            t01 = imgnose[i, j - 1]
            t02 = imgnose[i, j + 1]
            t10 = imgnose[i, j + 2]
            t11 = imgnose[i, j]
            t12 = imgnose[i - 2, j]
            t20 = imgnose[i - 1, j]
            t21 = imgnose[i + 1, j]
            t22 = imgnose[i + 2, j]
            templ =[t00,t01,t02,t10,t11,t12,t20,t21,t22]
            templ.sort()
            curimg[i,j]=templ[4]
    display('original', 2, [imgnose,curimg])
    return curimg
def cross3x3(imgnose):
    curimg = np.zeros((H,W),np.uint8)
    for i in range(1,H-2):
        for j in range(1,W-2):
            t00 = imgnose[i-1, j - 1]
            t01 = imgnose[i-1, j]
            t02 = imgnose[i-1, j + 1]
            t10 = imgnose[i, j-1]
            t11 = imgnose[i, j]
            t12 = imgnose[i, j+1]
            t20 = imgnose[i + 1, j-1]
            t21 = imgnose[i + 1, j]
            t22 = imgnose[i + 1, j+1]
            templ =[t00,t01,t02,t10,t11,t12,t20,t21,t22]
            templ.sort()
            curimg[i,j]=templ[4]
    display('original', 2, [imgnose,curimg])
    return curimg
def cross5x5(imgnose):
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
    display('original', 2, [imgnose,curimg])
    return curimg

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
    img = cv.imread("C:/Users/19845/Desktop/123.jpg", 0)
    (H, W) = img.shape
    print(H, W)
    img1=PepperandSalt(img,0.2)
    cv.imshow('PepperandSalt',img1)
    cv.waitKey(0)
    imgnose = np.zeros(img1.shape, np.uint8)
    imgnose[:] = img1[:]
    for i in range(1000):
        temp_x = np.random.randint(0, img1.shape[0])
        temp_y = np.random.randint(0, img1.shape[1])
        imgnose[temp_x][temp_y] = 255
    curcross = curcross(imgnose)
    cross3x3 = cross3x3(imgnose)
    cross5x5 = cross5x5(imgnose)
    Synthetic(H,W,curcross)
    Synthetic(H,W,cross3x3)
    Synthetic(H,W,curcross)

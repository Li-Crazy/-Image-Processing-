from numpy import *
from scipy import * 
import numpy as np 
import cv2 as cv

def SaltAndPepper(src,percetage):
    SP_NoiseImg=src
    SP_NoiseNum=int(percetage*src.shape[0]*src.shape[1])
    for i in range(SP_NoiseNum):
        randX=random.random_integers(0,src.shape[0]-1)
        randY=random.random_integers(0,src.shape[1]-1)
        if random.random_integers(0,1)==0:
            SP_NoiseImg[randX,randY]=0
        else:
            SP_NoiseImg[randX,randY]=255
    return SP_NoiseImg

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
        return curimg

if __name__ == "__main__":
    srcImage = cv.imread("C:/Users/19845/Desktop/123.jpg",0)
    (H, W) = srcImage.shape

    cv.namedWindow("Original image")
    cv.imshow("Original image", srcImage)

    SaltAndPepper_noiseImage = SaltAndPepper(srcImage, 0.1)  # 再添加10%的椒盐噪声
    cv.imshow("Add_SaltAndPepperNoise Image", SaltAndPepper_noiseImage)

    curimg = cross5x5(SaltAndPepper_noiseImage)


    cv.waitKey(0)
    cv.destroyAllWindows()


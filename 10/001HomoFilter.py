# Author imagean
#!/usr/bin/python
# -*- coding:utf-8
# opencv read image is BGR channel,and matplot read is RGB
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('C:/Users/19845/Desktop/lena2.jpg')
def homofilter(I):
    I = np.double(cv.cvtColor(I,cv.COLOR_RGB2GRAY))
    (m,n) = I.shape
    rL = 0.5
    rH = 2
    c =2
    d0 = 20
    I1 = np.log(I+1)
    FI = np.fft.fft2(I1)
    n1 =  m//2
    n2 =  n//2
    D = np.zeros((m,n))
    H = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            D[i,j]=((i-n1)**2+(j-n2)**2)
            H[i,j]=(rH-rL)*(np.exp(c*(-D[i,j]/(d0**2))))+rL

    I2 = np.fft.ifft2(H*FI)
    I3 = np.real(np.exp(I2))
    plt.subplot(1,2,1),plt.imshow(I,cmap='gray'),plt.xticks([]),plt.yticks([]),plt.title('Original Image')
    plt.subplot(1,2,2),plt.imshow(I3,cmap='gray'),plt.xticks([]),plt.yticks([]),plt.title('Homofilter Image')
    plt.show()
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

if __name__ == '__main__':


    (r,g,b)=cv.split(img) #颜色通道调整
    img = cv.merge([g,b,r])
    homofilter(img)


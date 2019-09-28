# Author image
#!/usr/python3/bin/python3.6
# -*- coding:utf-8

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
filename ='C:/Users/Zhang Bingjie/Pictures/LeNa.jpg'
image = cv.imread(filename)
image =cv.cvtColor(image,cv.COLOR_BGR2GRAY)
print(image.shape)
img = np.zeros(image.shape,np.uint8)

def Lookformin(subimg):
    (row,col)=subimg.shape
    min = 0
    for i in range(row):
        for j in range(col):
            if subimg[i,j]>0:
                min =subimg[i,j]
                break
    for i in range(row):
        for j in range(col):
            if subimg[i, j] < min and subimg[i,j]>0:
                min = subimg[i, j]
    return min


def geterode(img, kernel):
    (H,W) =img.shape
    erodeimg2 = np.zeros((H,W),np.uint8)
    print ("img.shape is (",H,W,")")
    (row,col)=kernel.shape
    print("kernel.shape(",row,col,")=\n", kernel)
    # 等于结构元素的子图像
    subimg = np.zeros((row, col), np.uint8)
    # 结构元素卷积运算原始图像
    for h in range(row//2, H-row//2):
        for w in range(col//2, W-col//2):
            #结构元素与对应点
            for i in range(-(row//2), row//2+1):
                for j in range(-(col//2), col//2+1):
                    subimg[row//2+i,col//2+j] = img[h+i,w+j]*kernel[row//2+i,col//2+j]

            smin = Lookformin(subimg)
            erodeimg2[h,w]=smin
    return erodeimg2

def change(image):
    (row,col)=image.shape
    for i in range(0,row):
        for j in range(0,col):
            if image[i,j]>=128:
                image[i,j]=1
            image[i,j]=0
if __name__ == '__main__':
    kernel = np.array([[0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0]], dtype=np.uint8)
    print(kernel)
    image=change(image)
    erodeimg1 = cv.erode(image, kernel, iterations=1)
    erodeimg2 = geterode(image, kernel)
    plt.figure(num='Basic Erode')
    plt.subplot(231),plt.imshow(image,cmap='gray'),plt.title("Original"),plt.xticks([]),plt.yticks([])
    plt.subplot(232), plt.imshow(erodeimg1, cmap='gray'), plt.title("CV Erode"), plt.xticks([]), plt.yticks([])
    plt.subplot(233), plt.imshow(erodeimg2, cmap='gray'), plt.title("My Erode"), plt.xticks([]), plt.yticks([])
    img[:] = (erodeimg2[:] + 1) / 128
    plt.subplot(234), plt.imshow(img, cmap='gray'), plt.title("Binarization"), plt.xticks([]), plt.yticks([])
    plt.subplot(235), plt.imshow(image-erodeimg1, cmap='gray'), plt.title("CV Edge"), plt.xticks([]), plt.yticks([])
    plt.subplot(236), plt.imshow(image-erodeimg2, cmap='gray'), plt.title("My Edge"), plt.xticks([]), plt.yticks([])
    plt.show()


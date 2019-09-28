# Author image
#!/usr/python3/bin/python3.6
# -*- coding:utf-8
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
filename ='/home/image/Pictures/lena256.jpg'
image = cv.imread(filename,0)
img = np.zeros(image.shape,np.uint8)

def getDilate(img, kernel):
    (H,W) =img.shape
    dilate2 = np.zeros((H, W), np.uint8)
    print("img.shape(H,W)=", H, W)
    (row,col)=kernel.shape
    # 等于结构元素的子图像
    subimg = np.zeros((row, col), np.uint8)
    # 结构元素卷积运算原始图像
    print("kernel.shape(row,col)", row, col)
    for h in range(row//2, H-row//2):
        for w in range(col//2, W-col//2):
            #结构元素与对应点
            for i in range(-(row//2), row//2+1):
                for j in range(-(col//2), col//2+1):
                    subimg[row//2+i,col//2+j] = img[h+i,w+j]*kernel[row//2+i,col//2+j]
            smax = subimg.max()
            dilate2[h, w] = smax
    return dilate2

if __name__ == '__main__':
    kernel = np.array([[0, 0, 1, 0, 0], [0, 1, 1, 1, 0],[1, 1, 1, 1, 1],[0, 1, 1, 1, 0], [0, 0, 1, 0, 0]], dtype=np.uint8)
    print(kernel)
    dilate1 = cv.dilate(image, kernel, iterations=1)
    dilate2 = getDilate(image, kernel)
    plt.figure(num='Basic Dilate')
    plt.subplot(231),plt.imshow(image,cmap='gray'),plt.title("Original"),plt.xticks([]),plt.yticks([])
    plt.subplot(232),plt.imshow(dilate1 ,cmap='gray'),plt.title("CV Dilate" ),plt.xticks([]),plt.yticks([])
    plt.subplot(233),plt.imshow(dilate2 ,cmap='gray'),plt.title("My Dilate"),plt.xticks([]),plt.yticks([])
    img[:] = (dilate1[:] + 1) / 128
    plt.subplot(234),plt.imshow(img ,cmap='gray'),plt.title("Binary Dilate"),plt.xticks([]),plt.yticks([])
    plt.subplot(235), plt.imshow(dilate1 -image, cmap='gray'), plt.title("CV edge "), plt.xticks([]), plt.yticks([])
    plt.subplot(236), plt.imshow(dilate2 -image, cmap='gray'), plt.title("My edge"), plt.xticks([]), plt.yticks([])

    plt.show()



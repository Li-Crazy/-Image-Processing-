# Author image
#!/usr/python3/bin/python3.6
# -*- coding:utf-8

import cv2 as cv
import matplotlib.pyplot as plt

filename ='C:/Users/19845/Desktop/cell3.jpg'
img = cv.imread(filename,0)
# 矩形：MORPH_RECT;
# 交叉形：MORPH_CROSS;
# 椭圆形：MORPH_ELLIPSE;
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
print(kernel)
# 腐蚀 erode : anchor=(-1,-1)锚点(内核中心点),iterations定义腐蚀次数
erosion = cv.erode(img,kernel,anchor=(-1,-1),iterations = 1)
# edge
img1 = img -erosion
# 膨胀 dilate :格式同上函数
dilation = cv.dilate(img,kernel,iterations = 1)
#开运算：先腐蚀，再膨胀，可清除一些小东西(亮的)，放大局部低亮度的区域
tophat1 = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
#闭运算：先膨胀，再腐蚀，可清除小黑点
tophat2 = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)

plt.subplot(231),plt.imshow(img,cmap='gray'),plt.title("lena.jpg(Original)"),plt.xticks([]),plt.yticks([])
plt.subplot(232),plt.imshow(erosion,cmap='gray'),plt.title("Erosion image "),plt.xticks([]),plt.yticks([])
plt.subplot(233),plt.imshow(img1,cmap='gray'),plt.title("Original-Erosion=Edge"),plt.xticks([]),plt.yticks([])
plt.subplot(234),plt.imshow(dilation,cmap='gray'),plt.title("Dilate"),plt.xticks([]),plt.yticks([])
plt.subplot(235),plt.imshow(tophat1,cmap='gray'),plt.title("cv.MORPH_OPEN"),plt.xticks([]),plt.yticks([])
plt.subplot(236),plt.imshow(tophat2,cmap='gray'),plt.title("cv.MORPH_CLOSE"),plt.xticks([]),plt.yticks([])

plt.show()

# Author imagean
#!/usr/bin/python
# -*- coding:utf-8
import cv2 as cv
import numpy as np
from  matplotlib import pyplot as plt
img2 = np.zeros((256,256,3), np.uint8)
img1 = cv.imread("C:/Users/19845/Desktop/1.jpg")
img2[:] = 255 - img1[:]


imgcolor = cv.imread("C:/Users/19845/Desktop/1.jpg")
imgtemp = np.zeros((imgcolor.shape[0],imgcolor.shape[1],3),np.uint8)
(b,g,r) = cv.split(imgcolor)
imgcolor= cv.merge((r,g,b))
imgtemp[:,:,:] = 255 -imgcolor[:,:,:]
img =[img1,img2,imgcolor,imgtemp]
titles =['256-gary image','oppsite image','24-bit image ','opposite image']
for i in range(4):
    plt.subplot(1,4,i+1)
    plt.imshow(img[i])
    plt.yticks()
    plt.xticks()
    plt.title(titles[i])
plt.show()


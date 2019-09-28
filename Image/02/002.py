 # Author imagean
#!/usr/bin/python
# -*- coding:utf-8
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
#cv.namedWindow('image1')
img1 = cv.imread("C:/Users/19845/Desktop/02gaussian.jpg",1)
print(img1.shape)
initrows = img1.shape[0]
initcols = img1.shape[1]
initcross = img1.shape[2]
print("Image.x=",initrows)
print("Image.y=",initcols)
print("Image.channel=",initcross)
img2 = np.zeros((initrows,initcols),dtype=img1.dtype)
b = np.zeros((initrows,initcols), dtype=img1.dtype)
g = np.zeros((initrows,initcols), dtype=img1.dtype)
r = np.zeros((initrows,initcols), dtype=img1.dtype)
b=img1[:,:,0]
g=img1[:,:,1]
r=img1[:,:,2]
print('blue=',b,'\ngreen=',g,'\nred=',r)
for i in range(0,initrows):
   for j in range(0,initcols):
       img2[i,j] = 0.114*img1[i,j,0]+0.587*img1[i,j,1]+0.299*img1[i,j,2]
img2[:]= 0.114*b +0.587* g + 0.299 *r
#print img2[:,:]
cv.imshow('img1',img1)
cv.imwrite("/home/imagean/Pictures/messigray.jpg",img2)
print(img2.shape)
print(img2.size)
#cv.imshow('image1', img1)
cv.waitKey(0)
cv.imshow('img2',img2)
cv.imwrite("ruiruigray.jpg",img2)
cv.waitKey(0)
cv.destroyAllWindows()

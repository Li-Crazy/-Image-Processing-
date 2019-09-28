# Author imagean
#!/usr/bin/python
# -*- coding:utf-8

import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread("C:/Users/19845/Desktop/1.jpg", 2)

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])
plt.show()

cv.waitKey(0)
img2 = img1 = img = cv.imread("C:/Users/19845/Desktop/1.jpg",1)
cv.imshow('My win_0',img)
cv.waitKey(0)
cv.destroyAllWindows()
for i in range(10,140):
   for j in range(30,160):
        img.itemset((i,j,2),255)

cv.imshow('My win_1',img)
img1[:,:,2]=0
b,g,r=cv.split(img1)  # The opposite operation is cv.merge(b,g,r)
# set red channel =0
cv.waitKey(0)
cv.imshow('My win_2',img1)


cv.waitKey(0)
cv.destroyAllWindows()



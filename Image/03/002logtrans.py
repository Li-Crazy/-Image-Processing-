# Author imagean
#!/usr/bin/python
# -*- coding:utf-8
import cv2 as cv
import numpy as np

img = cv.imread("C:/Users/19845/Desktop/02gaussian.jpg",0)
imgtrans = np.zeros((img.shape),np.uint8)
print(img.shape)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        imgtrans[i,j] = (2*(np.log(1+img[i,j])))% 256
cv.imshow('img',img)
cv.imshow('imgtrans',imgtrans)

cv.waitKey(0)
cv.destroyAllWindows()

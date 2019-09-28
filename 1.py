# Author imagean
#!/usr/bin/python
# -*- coding:utf-8
import cv2 as cv
import numpy as np
from random import randint
img = np.zeros((256,256,3),np.uint8)
img1= np.zeros((256,256),np.uint8)
for i in range(0,3):
    #a = [randint(1,255) for k in range(256)]
    for m in range(255):
        for n in range(255):
            img[m,n,i]= randint(0,255)
    cv.imshow('Image - 3 channel',img)
    cv.waitKey(0)
    cv.destroyAllWindows()

cv.waitKey(0)
img1 = img [:,:,1]
cv.imshow('Image - 3 channel', img1)
cv.waitKey(0)

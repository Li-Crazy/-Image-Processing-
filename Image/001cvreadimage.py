# Author imagean
#!/usr/bin/python
# -*- coding:utf-8 -*-

import cv2 as cv
#cv2 read image ,return Mat type and (BGR space )3-channel
img = cv.imread("C:/Users/19845/Desktop/lena2.jpg")
# cv2.COLOR_X2Y, X,Y = RGB, BGR, GRAY, HSV, YCrCb, XYZ, Lab, Luv, HLS
print("cv2 read image img:How big of image=",img.shape)
print("cv2 read image img:How much pixel numbers=",img.size)
print("cv2 read image img:what is type of image=",img.dtype)
cv.imshow('image cv.WINDOWS_NORMAL',img)
cv.waitKey(0)
cv.destroyAllWindows()



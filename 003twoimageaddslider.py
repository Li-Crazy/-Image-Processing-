# Author imagean
#!/usr/bin/python
# -*- coding:utf-8
# opencv read image is BGR channel,and matplot read is RGB

import cv2 as cv
import numpy as np
cv.namedWindow('image')
def nothing(x):
    pass
#two images sub
messia= cv.imread("C:/Users/19845/Desktop/1.jpg")        #(656X978)
maladona2 = cv.imread("C:/Users/19845/Desktop/3.jpg")        #(468X620)
#resize image's size ,and two image is the same size
print (maladona2.shape[1],maladona2.shape[0])
messias =cv.resize(messia,(maladona2.shape[1],maladona2.shape[0]))      #468 X 620
imgws = np.zeros(messia.shape,np.uint8)
cv.imshow('image', maladona2)

cv.createTrackbar('Threshold','image',0,100,nothing)
thresholds = cv.getTrackbarPos('Threshold', 'image')

while(thresholds >= 0) & (thresholds <=100):
    k = cv.waitKey(1)&0xFF
    if k == 27:
        thresholds = -1
    else:
        if (thresholds == cv.getTrackbarPos('Threshold','image')):
            pass
        else:
            thresholds = cv.getTrackbarPos('Threshold', 'image')
            lweight = float(thresholds)/100.0
            rweight = 1-lweight
            print('thresholds=',thresholds,'lweight=',lweight,'rweight=',rweight)
            imgws = np.uint8(messias * lweight+maladona2 * rweight)
            cv.imshow('image', imgws)

cv.destroyAllWindows()


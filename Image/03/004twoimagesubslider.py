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
backs= cv.imread("/home/image/Pictures/backsence.jpg")        #(402X312)
peoples = cv.imread("/home/image/Pictures/people.jpg")        #(402X313)
#resize image's size ,and two image is the same size
people =cv.resize(peoples,(backs.shape[1],backs.shape[0]))      #402 X 312
imgws = np.zeros(people.shape,np.uint8)


cv.createTrackbar('Threshold','image',0,100,nothing)
cv.imshow('image',imgws)
thresholds = cv.getTrackbarPos('Threshold', 'image')

while(thresholds >= 0) & (thresholds <=100):
    cv.imshow('image', imgws)
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
            imgws = np.uint8(people * lweight- backs * rweight)
cv.waitKey(27)
cv.destroyAllWindows()


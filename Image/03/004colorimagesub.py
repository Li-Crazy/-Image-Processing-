# Author imagean
#!/usr/bin/python
# -*- coding:utf-8
import cv2 as cv
def nothing(x):
    pass
flag = True
cv.namedWindow('image')
img2 = img1 = cv.imread("/home/image/Pictures/messi.jpg",1)
cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)
cv.imshow('image', img1)
r = cv.getTrackbarPos('R', 'image')
g = cv.getTrackbarPos('G', 'image')
b = cv.getTrackbarPos('B', 'image')

while(flag):
    k = cv.waitKey(1)&0xFF
    if k == 27:
        break
    else:
        if (r == cv.getTrackbarPos('R', 'image')) & (g == cv.getTrackbarPos('G', 'image')) & (b == cv.getTrackbarPos('B', 'image')):
            pass
        else:
            r = cv.getTrackbarPos('R', 'image')
            g = cv.getTrackbarPos('G', 'image')
            b = cv.getTrackbarPos('B', 'image')
            img2[:,:,:] = img1[:,:,:]-[b,g,r ]
            cv.imshow('image', img2)
cv.destroyAllWindows()
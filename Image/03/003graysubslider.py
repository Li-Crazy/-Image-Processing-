# Author imagean
#!/usr/bin/python
# -*- coding:utf-8
import cv2 as cv

def nothing(x):
    pass
flag = True
cv.namedWindow('image')
img2 = img1 = cv.imread("C:/Users/Zhang Bingjie/Pictures/kenan1.jpg",0)
print(img1.shape[0],img1.shape[1])
cv.createTrackbar('Gray','image',20,255,nothing)
cv.imshow('image', img1)
graydegree = cv.getTrackbarPos('Gray', 'image')
print(graydegree)
while(flag):
    k = cv.waitKey(1)&0xFF
    if k == 27:
        break
    else:
        if (graydegree == cv.getTrackbarPos('Gray', 'image')):
            pass
        else:
            graydegree = cv.getTrackbarPos('Gray', 'image')
            if graydegree ==255:
                img2[:] = 255- img1[:]
            else:
                img2[:] =img1[:]-graydegree
    cv.imshow('image', img2)
cv.destroyAllWindows()




# Author imagean
#!/usr/bin/python
# -*- coding:utf-8
# opencv read image is BGR channel,and matplot read is RGB
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
#two images sub
backs= cv.imread("C:/Users/19845/Desktop/02gaussian.jpg")          #(306 X 249)
people = cv.imread("C:/Users/19845/Desktop/02gaussian.jpg")           #(291 X 241)
#resize image's size ,and two image is the same size
backsup = cv.resize(backs,(people.shape[1],people.shape[0]))      #(291 X 241)
cv.imshow("suns image",people*0.7 - backsup*0.3)
rowb = backsup.shape[0]
colb = backsup.shape[1]
rowp = people.shape[0]
colp = people.shape[1]
if (backsup.shape[2]) & (people.shape[2]) & (rowb == rowp) & (colb == colp):
    imgb = np.zeros((rowp, colp), np.uint8)
    (b1,g1,r1) = cv.split(backsup)
    imgb[:] = 0.114*b1 +0.587*g1 + 0.299*r1
    (b2,g2,r2) = cv.split(people)
    imgp = np.zeros((rowp, colp), np.uint8)
    imgp[:] = 0.114*b2 +0.587*g2 + 0.299*r2
    threshold=127
for i in range(rowp):
    for j in range(colp):
        if imgp[i,j] < threshold:
            imgp[i,j] = 0
        else:
            imgp[i,j] = 255
        if imgb[i,j] < threshold:
            imgb[i,j] = 0
        else:
            imgb[i,j] = 255
images = [people,backsup]
titles = ['all sence ','back sence ']
for i in range(2):
   plt.subplot(1,2,i+1),plt.imshow(images[i])
   plt.title(titles[i])
   plt.xticks([]),plt.yticks([])
plt.show()
cv.imshow("two vulume-1",imgb)
cv.imshow("two vulume-2",imgp)
cv.imshow("two image sub",imgb - imgp)
cv.waitKey(0)
cv.destroyAllWindows()


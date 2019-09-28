# Author imagean
#!/usr/bin/python
# -*- coding:utf-8
# opencv read image is BGR channel,and matplot read is RGB
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

names = "C:/Users/19845/Desktop/01original.jpg"
img = cv.imread(names,0)
(H,W)=img.shape
pixel = H * W

def display(files):
    cv.namedWindow("hist-imgs", 0)
    cv.resizeWindow("hist-imgs",3*H,W)
    cv.imshow("hist-imgs", np.hstack(files))

def opencvdef(img):
    # opencv own's equlization function
    t1 = cv.getTickCount()
    eq = cv.equalizeHist(img)
    t2 = cv.getTickCount()
    T1 = (t2 - t1) / cv.getTickFrequency()
    print("Opencv Histogram() Time consuming is ", T1,'second')
    files.append(eq)

def own(img):
    # bins is gray volume ,wide 0~255 ,hist is  every gray volume numbers
    t1 =cv.getTickCount()
    hist,bins = np.histogram(img.flatten(), 256, [0, 255])
    LUT = np.zeros(256,np.uint8)
    LUT[0] =1.0 *hist[0] / pixel *255
    sumnums = hist[0]
    for i in range(1,256):
        #s[i]= sum of gray form 0 to i
        sumnums =sumnums +hist[i]
        # LUT is equliztion array  = (255 X s[i])
        LUT[i] = np.uint8(1.0*sumnums /pixel *255)
    temps =np.zeros((H,W),np.uint8)
    for i in range(H ):
        for j in range(W ):
            temps[i,j] =LUT[img[i,j]]
    t2 = cv.getTickCount()
    T2 = (t2 - t1) / cv.getTickFrequency()
    print("Own Histogram() Time consuming is ", T2,'second')

    files.append(temps)
    pltshow(files)

    #display(files)
    #cv.waitKey(0)

def pltshow(files):
    for i in range(3):
        plt.subplot(2,3,i+1),plt.imshow(files[i], cmap='gray', interpolation='bicubic')
        plt.xticks([]),plt.yticks([])
    for i in range(3):
        hist, bins = np.histogram(files[i].flatten(), 256, [0, 255])
        plt.subplot(2,3,4+i),plt.hist(files[i].flatten(), 256, [0, 255])
        plt.xlim(0, 255),plt.ylim(0, hist.max()+1)
    plt.show()

if __name__ == '__main__':
    files =[img]
    opencvdef(img)
    own(img)







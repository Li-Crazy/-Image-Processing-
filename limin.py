import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
#cv.namedWindow('image1')
img1 = cv.imread("C:/Users/19845/Desktop/lena2.jpg",1)
img2 = cv.imread("C:/Users/19845/Desktop/lena_slat.jpg",1)
print(img1.shape)
print(img2.shape)
initrows = img1.shape[0]
initcols=img1.shape[1]
# print(initrows)
# initrows1 = img2.shape[0]
# initcols1=img2.shape[1]
img5 = np.zeros(img1.shape,np.uint8)
for i in range(initrows):
    for j in range(initcols):
        img5[i,j] = img1[i,j] + img1[i,j]
cv.imshow("img5",img5)
cv.waitKey(0)
cv.destroyAllWindows()

for i in range(H):
    for j in range(W):
        Hist[img[i,j]]+=1
            for i in range(256):
            HistP[i] =Hist[i]/Pixelsum for i in range(1,256):
            HistPSUM[i] =HistP[i]+HistPSUM[i-1]
        for i in range(256):
            EqHist[i] =HistPSUM[i]*255
            for i in range(H):
                for j in range(W):
                    Newimg[i,j]= EqHist[img[i,j]]
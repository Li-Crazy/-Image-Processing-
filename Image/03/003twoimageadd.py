# Author imagean
#!/usr/bin/python
# -*- coding:utf-8
# opencv read image is BGR channel,and matplot read is RGB

import cv2 as cv
from matplotlib import pyplot as plt
import  numpy as np

# two images addweighted and simple add
imgbottle = cv.imread("/home/image/Pictures/bottle.png")
(r,g,b)= cv.split(imgbottle)
img1 = cv.merge([b,g,r])
imgcloud = cv.imread("/home/image/Pictures/cloud.png")
(r,g,b)= cv.split(imgcloud)
img2 = cv.merge([b,g,r])

img3 = cv.addWeighted(img1,0.7,img2,0.3,0)
img4 = np.zeros(img3.shape,np.uint8)
img4[:,:,:] = img1[:,:,:] + img2[:,:,:]
images = [img1,img2,img3,img4]
titles = ['bottle','cloud ','  maxture Image',' simple + Image']
for i in range(4):
   plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
   plt.title(titles[i])
   plt.xticks([]),plt.yticks([])
plt.show()


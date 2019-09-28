# Author imagean
#!/usr/bin/python
# -*- coding:utf-8
# opencv read image is BGR channel,and matplot read is RGB

import cv2 as cv
from PIL import Image
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import numpy as np

filename ='/home/imagean/Pictures/bottle.png'

# PIL.open image
pil_img = Image.open(filename)  #get a image object
pil_img = np.array(pil_img)      #transform into numpy type
print 'type(pil_img)=,',type(pil_img),'pil_img.shape=',pil_img.shape
# cv.imread image (BGR channel) = PIL.open
cv_img = cv.imread(filename)
print 'type(cv_img)=,',type(cv_img),'cv_img.shape=',cv_img.shape
# matplotlib.image.imread iamge (RGB channel)
plt_img = mpimg.imread(filename)
print 'type(plt_img)=,',type(plt_img),'plt_img.shape=',plt_img.shape


# cv_BGR space 2 plt_RGB space
(r, g, b)=cv.split(cv_img) #split cv BGR
img=cv.merge([b,g,r])   #merge plt RGB
images = [pil_img ,cv_img ,plt_img, img ]
titles = ['pil_img','cv_img','plt_img','tans_img']
# imshow in matplotlib space

for i in xrange(4):
   plt.subplot(2,2,i+1),plt.title(titles[i])
   plt.imshow(images[i])
   plt.xticks([]),plt.yticks([])
plt.show()
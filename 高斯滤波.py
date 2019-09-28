import cv2 as cv
import numpy as np
import math

path ="C:/Users/19845/Desktop/original.jpg"
img = cv.imread(path)
(H,W,channel) =img.shape
print('image high is:',H,'pixel && image whith is:',W,'pixel')

def dis(title,total,files):
    cv.namedWindow(title, 0)
    cv.resizeWindow(title,total * H, W)
    cv.imshow(title,np.hstack(files))
    cv.waitKey(0)

def Gasuu(gaus,size,sigma):
    # This is Pi
    Pi = 4.0 * math.atan(1.0)
    center = int(size / 2)
    sum =0.0
    for i in range(0,size):
        for j in range(0,size):
            # This is a gaussian Kernel
            deltax = (i- center)*(i- center)
            deltay = (j- center)*(j- center)
            sigma2 =2.0 *(sigma *sigma)
            temp1 = 1.0 /(Pi*sigma2)
            temp2 = math.exp(-((deltax+deltay))/sigma2)
            gaus[i,j]=temp1 * temp2
            sum =sum +gaus[i,j]
    for i in range(0, size):
        for j in range(0, size):
            gaus[i,j] =gaus[i,j] /sum
    print(gaus)
    return gaus

def Gasufilter(imgs,gaus,size):
    imggasu = np.zeros((H,W),np.uint8)
    for i in range(int(size/2),int(H-size/2)):
        for j in range(int(size/2),int(H-size/2)):
            sum =0.0
            for k in range(size):
                for l in range(size):
                    sum = sum + gaus[k,l]*imgs[i-k,j-l]
            imggasu[i,j] = np.uint8(sum)
    files =[imgs,imggasu]
    dis("Gaussian denoise image",files.__len__(),files)


# def LoG(imgs,gaus):
#     ker = np.zeros((H, W),np.uint8)
#     print(gaus)
#     for i in range(2,H - 2):
#         for j in range(2,W - 2):
#             for m in range(0,5):
#                 for n in range(0,5):
#                     ker[i,j] += gaus[m,n] * imgs[i-2+m,j-2+n]
#                     if (abs(ker[i,j]) > 255):
#                         ker[i,j] = 255
#                     else:
#                         ker[i,j] = abs(ker[i,j])
#     dis('original', 2, [imgs,ker])

def display(title,img):
    cv.imshow(title,img)
    cv.waitKey()
    cv.destroyAllWindows()



if __name__ == '__main__':
    imgs = np.zeros((H, W), np.uint8)
    if channel == 3: #to 256 gray
        (b, g, r) = cv.split(img)
        imgs[:] = 0.114 * b + 0.587 * g + 0.299 * r
    else:
        imgs = img
    #gaussian template :kernelsize is templte size and sigma
    kernelsize = 5
    kernelsigma = 1
    s = (kernelsize, kernelsize)
    # gaussian template
    print(s)
    gaus = np.zeros(s)
    # calculate gaussian template
    ga = Gasuu(gaus,kernelsize,kernelsigma)
    # Call Gasufilter
    Gasufilter(imgs, ga, kernelsize)
    # Call sobel calculate

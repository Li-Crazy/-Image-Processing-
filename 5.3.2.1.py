'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/4/16 8:37
@Software: PyCharm
@File    : 5.3.2.1.py
'''
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
path = "C:/Users/19845/Desktop/"
originalfiles = "sandglass.png"

def displt(files,len,titles):
    m = len /3
    print(m)
    for i in range(len):
        plt.subplot(m,len/2,i+1),plt.imshow(files[i],cmap='gray')
        plt.xticks([]),plt.yticks([])
        plt.title(titles[i])
    plt.show()

def fft(img):
    f=np.fft.fft2(img)
    f1shift= np.fft.fftshift(f)#中心到原点
    # Four angle imshow()
    f1 =np.log(np.abs(f))#中心点对应赋值
    # Central point imshow()
    fs1=np.log(np.abs(f1shift))
    return [f1shift,f1,fs1]

#互换0和1
def passfilter(filterf):
    (rows, cols) = filterf.shape
    # np.ones() is set all uint of 2-Array value  is 1
    highmask = np.ones((rows,cols), np.uint8)
    highmask[rows//2-40:rows//2+40,cols//2-40:cols//2+40] = 0
# highpass filter is Convolution1_pulsenoise
    f1 = filterf*highmask
    ifs1 = np.fft.ifftshift(f1)
    highf = np.log(np.abs(np.fft.ifft2(ifs1)))
    # np.zeros() is set all uint of 2-Array value  is 0
    lowmask = np.zeros((rows, cols), np.uint8)
    lowmask[rows//2-40:rows//2+40,cols//2-40:cols//2+40] = 1
# lowpass filter is Convolution
    f2 = filterf * lowmask
    ifs2 = np.fft.ifftshift(f2)
    lowf = np.log(np.abs(np.fft.ifft2(ifs2)))
# pass filter
    mask1 = np.ones(filterf.shape, np.uint8)
    mask1[rows // 2 - 40:rows // 2 + 40, cols // 2 - 40:cols // 2 +40] = 0
    mask2 = np.zeros(filterf.shape, np.uint8)
    mask2[rows // 2 - 80:rows // 2 + 80, cols // 2 - 80:cols // 2 + 80] = 1
    mask = mask1 * mask2
    f3 = filterf * mask
    ifs3 = np.fft.ifftshift(f3)
    passf = np.log(np.abs(np.fft.ifft2(ifs3)))
# Band fliter
    mask1 = np.zeros(filterf.shape, np.uint8)
    mask1[rows // 2 - 10:rows // 2 + 10, cols // 2 - 10:cols //2 + 10] = 1
    mask2 = np.ones(filterf.shape, np.uint8)
    mask2[rows // 2 - 80:rows // 2 + 80, cols //2 - 80:cols // 2 + 80] = 0
    mask = mask1 * mask2
    f4 = filterf * mask
    ifs4 = np.fft.ifftshift(f4)
    #bandf = np.log(np.abs(np.fft.ifft2(ifs4)))
    files=[lowf,highf,passf]
    return files

if __name__ == '__main__':
    img_ori = cv.imread(path + originalfiles, 0)
    (H, W) = img_ori.shape
    imgfft = fft(img_ori)
    allimg = passfilter(imgfft[0])
    allimg.insert(0,img_ori)
    allimg.insert(1,imgfft[1])
    allimg.insert(2,imgfft[2])

    len1= allimg.__len__()
    ti=['Original','Bofore shift','After shift','Low pass','High pass','Pass']
    displt(allimg,len1,ti)

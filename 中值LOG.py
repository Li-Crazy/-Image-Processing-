# Author imagean
# !/usr/bin/python
# -*- coding:utf-8
# opencv read image is BGR channel,and matplot read is RGB

import cv2 as cv
import numpy as np
img = cv.imread("C:/Users/19845/Desktop/123.jpg",0)
(H,W) =img.shape
print (H,W)

def display(title,imagenum,files):
    cv.namedWindow(title, 0)
    cv.resizeWindow(title,imagenum*H,W)
    cv.imshow(title, np.hstack(files))
    cv.waitKey(0)

def salt(img):
    img_copy = np.zeros((H,W),np.uint8)
    for i in range(0,H):
        for j in range(0,W):
          img_copy[i][j]=img[i][j]
    #用3*3的中值滤波器
    step=3
    def m_filter(x,y):
        sum_s=[]
        for k in range(-int(step/2),int(step/2)+1):
            for m in  range(-int(step/2),int(step/2)+1):
                sum_s.append(img[x+k][y+m])
        sum_s.sort()
        return sum_s[(int(step*step/2)+1)]

    for i in range(int(step/2),img.shape[0]-int(step/2)):
        for j in range(int(step/2),img.shape[1]-int(step/2)):
            img_copy[i][j]=m_filter(i,j)
    display('original', 2, [img,img_copy])

# def curcross(img,imgnose):
#     t1 = cv.getTickCount()
#     curimg = np.zeros((H,W),np.uint8)
#     for i in range(2,H-3):
#         for j in range(2,W-3):
#             t00 = imgnose[i, j - 2]
#             t01 = imgnose[i, j - 1]
#             t02 = imgnose[i, j + 1]
#             t10 = imgnose[i, j + 2]
#             t11 = imgnose[i, j]
#             t12 = imgnose[i - 2, j]
#             t20 = imgnose[i - 1, j]
#             t21 = imgnose[i + 1, j]
#             t22 = imgnose[i + 2, j]
#             templ =[t00,t01,t02,t10,t11,t12,t20,t21,t22]
#             templ.sort()
#             curimg[i,j]=templ[4]
#
#     t2 = cv.getTickCount()
#     print("template calc spend time is =", (t2 - t1) / cv.getTickFrequency(), 'second')
#     display('original', 3, [img,imgnose,curimg])
#     return curimg
#
# # def LoG(curimg):
# #     t1 = cv.getTickCount()
# #     ker = np.zeros((H, W),np.uint8)
# #     template = np.mat([[-2, -4, -4, -4, -2],
# #                        [-4, 0, 8, 0, -4],
# #                        [-4, 8, 24, 8, -4],
# #                        [-4, 0, 8, 0, -4],
# #                        [-2, -4, -4, -4, -2]])
# #
# #     for i in range(2,H - 2):
# #         for j in range(2,W - 2):
# #             for m in range(0,5):
# #                 for n in range(0,5):
# #                     ker[i,j] += template[m,n] * curimg[i-2+m,j-2+n]
# #                     if (abs(ker[i,j]) > 255):
# #                         ker[i,j] = 255
# #                     else:
# #                         ker[i,j] = abs(ker[i,j])
# #     t2 = cv.getTickCount()
# #     print("template calc spend time is =", (t2 - t1) / cv.getTickFrequency(), 'second')
# #     display('original', 2, [curimg,ker])
#
#
#
# def cross3x3(img,imgnose):
#     t1 = cv.getTickCount()
#     curimg = np.zeros((H,W),np.uint8)
#     for i in range(1,H-2):
#         for j in range(1,W-2):
#             t00 = imgnose[i-1, j - 1]
#             t01 = imgnose[i-1, j]
#             t02 = imgnose[i-1, j + 1]
#             t10 = imgnose[i, j-1]
#             t11 = imgnose[i, j]
#             t12 = imgnose[i, j+1]
#             t20 = imgnose[i + 1, j-1]
#             t21 = imgnose[i + 1, j]
#             t22 = imgnose[i + 1, j+1]
#             templ =[t00,t01,t02,t10,t11,t12,t20,t21,t22]
#             templ.sort()
#             curimg[i,j]=templ[4]
#     t2 = cv.getTickCount()
#     print("template calc spend time is =", (t2 - t1) / cv.getTickFrequency(), 'second')
#     display('original', 3, [img,imgnose,curimg])
#
# def cross5x5(img,imgnose):
#     t1 = cv.getTickCount()
#     curimg = np.zeros((H,W),np.uint8)
#     for i in range(2,H-3):
#         for j in range(2,W-3):
#             t00 = imgnose[i-2,j-2]
#             t01 = imgnose[i-2,j-1]
#             t02 = imgnose[i-2,j]
#             t03 = imgnose[i-2,j+1]
#             t04 = imgnose[i-2,j+2]
#             t10 = imgnose[i-1, j - 2]
#             t11 = imgnose[i-1, j - 1]
#             t12 = imgnose[i-1, j]
#             t13 = imgnose[i-1, j + 1]
#             t14 = imgnose[i-1, j + 2]
#             t20 = imgnose[i , j - 2]
#             t21 = imgnose[i , j - 1]
#             t22 = imgnose[i , j]
#             t23 = imgnose[i , j + 1]
#             t24 = imgnose[i , j + 2]
#             t30 = imgnose[i+1, j - 2]
#             t31 = imgnose[i+1, j - 1]
#             t32 = imgnose[i+1, j]
#             t33 = imgnose[i+1, j + 1]
#             t34 = imgnose[i+1, j + 2]
#             t40 = imgnose[i+2, j - 2]
#             t41 = imgnose[i+2, j - 1]
#             t42 = imgnose[i+2, j]
#             t43 = imgnose[i+2, j + 1]
#             t44 = imgnose[i+2, j + 2]
#             templ =[t00,t01,t02,t03,t04,t10,t11,t12,t13,t14,t20,t21,t22,t23,t24,t30,t31,t32,t33,t34,t40,t41,t42,t43,t44]
#             templ.sort()
#             curimg[i,j]=templ[12]
#     t2 = cv.getTickCount()
#     print("template calc spend time is =", (t2 - t1) / cv.getTickFrequency(), 'second')
#     display('original', 3, [img,imgnose,curimg])


if __name__ == '__main__':
    imgnose = np.zeros(img.shape,np.uint8)
    imgnose[:] = img[:]
    for i in range(1000):
        temp_x = np.random.randint(0, img.shape[0])
        temp_y = np.random.randint(0, img.shape[1])
        imgnose[temp_x][temp_y] = 255
    curimg = curcross(img,imgnose)
    cv.imshow('curimg',curimg)
    # LoG(curimg)
    salt(curimg)
    cross3x3(img,imgnose)
    cross5x5(img,imgnose)


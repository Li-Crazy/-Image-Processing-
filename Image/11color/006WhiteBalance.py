# Author image
# !/usr/python3/bin/python3.6
# -*- coding:utf-8
# opencv read image is BGR channel,and matplot read is RGB
import cv2 as cv
import numpy as np

def dis(f,H,W):
    cv.namedWindow("imgs", 0)
    cv.resizeWindow("imgs",W*f.__len__(),H )
    cv.imshow('imgs',np.hstack(f))
    cv.waitKey()


if __name__ == '__main__':
    img = cv.imread('/home/image/Pictures/sence.jpg')
    (B, G, R)= cv.split(img)
    (H, W, channel)= img.shape
    print(B.shape)
    sum = np.zeros(B.shape)
    for i in range(H):
        for j in range(W):
            sum[i][j] = int(B[i][j]) + int(G[i][j]) + int(R[i][j])
    (hists, bins) = np.histogram(sum.flatten(), 766, [0, 766])
    Y = 765
    num, key = 0, 0
    while Y >= 0:
        num += hists[Y]
        if num > H * W * 0.01 / 100:
            key = Y
            break
        Y = Y - 1

    sum_b, sum_g, sum_r = 0, 0, 0
    time = 0
    for i in range(H):
        for j in range(W):
            if sum[i][j] >= Y:
                sum_b += B[i][j]
                sum_g += G[i][j]
                sum_r += R[i][j]
                time = time + 1

    avg_b = sum_b / time
    avg_g = sum_g / time
    avg_r = sum_r / time

    for i in range(H):
        for j in range(W):
            B[i][j] = B[i][j] * 255 / avg_b
            G[i][j] = G[i][j] * 255 / avg_g
            R[i][j] = R[i][j] * 255 / avg_r
            if B[i][j] > 255:
                B[i][j] = 255
            if B[i][j] < 0:
                B[i][j] = 0
            if G[i][j] > 255:
                G[i][j] = 255
            if G[i][j] < 0:
                G[i][j] = 0
            if R[i][j] > 255:
                R[i][j] = 255
            if R[i][j] < 0:
                R[i][j] = 0

    img_0 = cv.merge([B, G, R])
    dis([img,img_0],H,W)
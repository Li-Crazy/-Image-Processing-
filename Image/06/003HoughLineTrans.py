# Author image
# !/usr/bin/python
# -*- coding:utf-8
# opencv read image is BGR channel,and matplot read is RGB



import sys
import numpy as np
import cv2
import math
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def HTline(img, steptheta=1, steprho=1):
    rows, cols = img.shape
    # 图像中可能出现的最大长度
    L = round(math.sqrt(pow(rows, 2.0) + pow(cols, 2.0))) + 1
    #  参数坐标系累加器阵列
    numtheta = int(180.0 / steptheta)
    numrho = int(2 * L / steprho) + 1
    accumulator = np.zeros((numrho, numtheta), np.int32)
    # 建立字典，存储点坐标
    accuDict = {}
    for k1 in range(-L, L + 1, steprho):
        for k2 in range(numtheta):
            accuDict[(k1, k2)] = []
    # 投票计数
    for y in range(rows):
        for x in range(cols):
            if img[y][x] == 255:
                for m in range(numtheta):
                    rho = round(x * math.cos(steptheta * m / 180.0 * math.pi) + y * math.sin(steptheta * m / 180.0 * math.pi))
                    accumulator[rho, m] += 1
                    accuDict[(rho, m)].append((x, y))  # 这里xy坐标得换过来
    return accuDict, accumulator


# 主函数
if __name__ == '__main__':
    img = cv2.imread('C:/Users/19845/PycharmProjects/Project/cell.jpg', 0)
    # canny 边缘检测
    edge = cv2.Canny(img, 50, 200)
    # 显示二值化边缘
    cv2.imshow('edge', edge)
    # 霍夫直线检测
    accuDict, accumulator = HTline(edge, 1, 1)
    # 计数器三维显示
    rows, cols = accumulator.shape
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X, Y = np.mgrid[0:rows:1, 0:cols:1]
    surf = ax.plot_wireframe(X, Y, accumulator, cstride=1, rstride=1, color='gray')
    ax.set_xlabel(u"$\\rho$")
    ax.set_ylabel(u"$\\theta$")
    ax.set_zlabel("accumulator")
    ax.set_zlim3d(0, np.max(accumulator))
    # 只画出投票数大于60的直线
    voteThresh = 60
    for r in range(rows):
        for c in range(cols):
            if accumulator[r][c] > voteThresh:
                points = accuDict[(r,c)]
                #print(points)
                cv2.line(img, points[0], points[len(points) - 1], (255), 2)  # 画线
    cv2.imshow("I", img)
    plt.show()
    cv2.waitKey(0)
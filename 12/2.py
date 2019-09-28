'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/5/22 19:52
@Software: PyCharm
@File    : 2.py
'''
import matplotlib.pyplot as plt
import cv2
im = cv2.imread("C:/Users/19845/Desktop/cell3.jpg")
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)


retval, im_at_fixed = cv2.threshold(im_gray, 50, 255, cv2.THRESH_BINARY)

"""固定阈值二值化
我们首先进行固定阈值二值化处理，固定阈值二值化处理利用cv2.threshold函数，此函数的原型为：
cv2.threshold(src, thresh, maxval, type[, dst]) -> retval, dst
其中:
src 为输入图像；
thresh 为阈值；
maxval 为输出图像的最大值；
type 为阈值的类型；
dst 为目标图像。"""

im_at_mean = cv2.adaptiveThreshold(im_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 10)

"""算术平法的自适应二值化
算术平均法的自适应二值化利用cv2.adaptiveThreshold实现，此函数的原型为：

cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst]) -> dst
其中：

src 为输入图像；
maxval 为输出图像的最大值；
adaptiveMethod 设置为cv2.ADAPTIVE_THRESH_MEAN_C表示利用算术均值法，设置为cv2.ADAPTIVE_THRESH_GAUSSIAN_C表示用高斯权重均值法；
thresholdType: 阈值的类型；
blockSize: b的值；
C 为从均值中减去的常数，用于得到阈值；
dst 为目标图像。"""

im_at_mean1 = cv2.adaptiveThreshold(im_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY, 5, 7)

"""高斯加权均值法自适应二值化
高斯加权均值法自适应二值化也是利用cv2.adaptiveThreshold， 此函数的原型与上述相同：

cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst]) -> dst
其中：

src 为输入图像；
maxval 为输出图像的最大值；
adaptiveMethod 设置为cv2.ADAPTIVE_THRESH_MEAN_C表示利用算术均值法，设置为cv2.ADAPTIVE_THRESH_GAUSSIAN_C表示用高斯权重均值法；
thresholdType: 阈值的类型；
blockSize: b的值；
C 为从均值中减去的常数，用于得到阈值；
dst 为目标图像。"""

plt.subplot(221), plt.imshow(im_gray, cmap='gray'), plt.title(
    "Original"), plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(im_at_fixed, cmap='gray'), plt.title(
    "Threshold"), plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(im_at_mean, cmap='gray'), plt.title(
    "Adaptive"), plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(im_at_mean1, cmap='gray'), plt.title(
    "Adaptive"), plt.xticks([]), plt.yticks([])
plt.show()


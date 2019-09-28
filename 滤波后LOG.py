import numpy as np
import cv2 as cv
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import scipy.signal as signal

def LoG(d,n):
    ker = np.zeros((n,n))
    c = int((n-1)/2)
    for i in range(n):
        for j in range(n):
            ker[i,j] = (((c-i)**2+(c-j)**2-2*d**2)/d**4*np.exp(-(((c-i)**2+(c-j)**2))/(2*d**2)))
    ker = ker + np.min(ker)
    ker = ker/np.sum(ker)
    return ker


# 生成高斯算子的函数
def func(x, y, sigma=1):
    return 100 * (1 / (2 * np.pi * sigma)) * np.exp(-((x - 2) ** 2 + (y - 2) ** 2) / (2.0 * sigma ** 2))


# 生成标准差为5的5*5高斯算子
suanzi1 = np.fromfunction(func, (5, 5), sigma=5)

# Laplace扩展算子
suanzi2 = np.array([[1, 1, 1],
                    [1, -8, 1],
                    [1, 1, 1]])

# 打开图像并转化成灰度图像
image = cv.imread("C:/Users/19845/Desktop/1.jpg",0)
image_array = np.array(image)

# 利用生成的高斯算子与原图像进行卷积对图像进行平滑处理
image_blur = signal.convolve2d(image_array, suanzi1, mode="same")

# 对平滑后的图像进行边缘检测
image2 = signal.convolve2d(image_blur, suanzi2, mode="same")

# 结果转化到0-255
image2 = (image2 / float(image2.max())) * 255

# 将大于灰度平均值的灰度值变成255（白色），便于观察边缘
image2[image2 > image2.mean()] = 255

# 显示图像
plt.subplot(2, 1, 1)
plt.imshow(image_array, cmap=cm.gray)
plt.axis("off")
plt.subplot(2, 1, 2)
plt.imshow(image2, cmap=cm.gray)
plt.axis("off")
plt.show()
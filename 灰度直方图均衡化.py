# coding=utf-8
'''
1.均衡化前的直方图和累计直方图
2.均衡化后的直方图和累计直方图
3.均衡化的函数用的是opencv中的equalizaHist
calcHist—计算图像直方图
函数原型：calcHist(images, channels, mask, histSize, ranges, hist=None, accumulate=None)
images：图像矩阵，例如：[image]
channels：通道数，例如：0
  mask：掩膜，一般为：None
histSize：直方图大小，一般等于灰度级数
ranges：横轴范围
4.计算图像直方图的函数用的是opencv中的calcHist
equalizeHist—直方图均衡化
函数原型： equalizeHist(src, dst=None)
src：图像矩阵
dst：默认即可
'''
import cv2 as cv
import numpy as np
def drawHist(hist):
    img = np.zeros((256, 256), np.uint8)
    r = max(hist) / 255#数组中最大值除以255
    for i in range(0, 256):
        hist[i] = hist[i] / r
        cv.line(img, (i, 255), (i, 255 - hist[i]), 255)
    return img

'''
img=cv.line(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
作用：给定一个图像img，连接点pt1和pt2的坐标，在图中画一条直线，color表明线的颜色
其中需要注意的是，点坐标(x, y)中，x代表图片的列，y代表图片的行

numpy.zeros 创建指定大小的数组，数组元素以 0 来填充：
numpy.zeros(shape, dtype = float, order = 'C')
shape	数组形状
dtype	数据类型，可选，uint8 无符号整数（0 to 255）
order	'C' 用于 C 的行数组，或者 'F' 用于 FORTRAN 的列数组
'''

img = cv.imread("C:/Users/19845/Desktop/123.jpg", 0)#0  灰度图模式
#使用opencv读取图像，直接返回numpy.ndarray 对象，通道顺序为BGR ，注意是BGR，通道值默认范围0-255。
hist1 = cv.calcHist([img],  # 计算图像的直方图
                     [0],  # 使用的通道数
                     None,  # 没有使用mask，掩膜
                     [256],  # it is a 1D histogram，直方图大小，一般等于灰度级数
                     [0.0, 255.0])#横轴范围
hist11 = hist1.cumsum()  # 累计直方图,求累计值不会改变原数组的值
hist111 = hist11.reshape(hist1.shape)  # reshape也不会改变原数组的值
# hist1是二维(ndim),hist11是一维
'''numpy.reshape 函数可以在不改变数据的条件下修改形状，格式如下： numpy.reshape(arr, newshape, order='C')
arr：要修改形状的数组
newshape：整数或者整数数组，新的形状应当兼容原有形状
order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'k' -- 元素在内存中的出现顺序。
'''
'''ndarray.shape 表示数组的维度，返回一个元组，这个元组的长度就是维度的数目，即 ndim 属性(秩)。
比如，一个二维数组，其维度表示"行数"和"列数"。
ndarray.shape 也可以用于调整数组大小。
'''

############均衡化后的投影值和累计值#######
equ = cv.equalizeHist(img)  # 均衡化
hist2 = cv.calcHist([equ],  # 计算图像的直方图
                     [0],  # 使用的通道
                     None,  # 没有使用mask
                     [256],  # it is a 1D histogram
                     [0.0, 255.0])
hist22 = hist2.cumsum()  # 累计直方图,求累计值不会改变原数组的值
hist222 = hist22.reshape(hist2.shape)  # reshape也不会改变原数组的值


a = drawHist(hist1)
a1 = drawHist(hist111)
cv.imshow("first", a)#均衡化前的直方图
cv.imshow("second", a1)#均衡化前的累计直方图
cv.imshow('img1',img)


b = drawHist(hist2)
b1 = drawHist(hist222)
cv.imshow("third", b)#均衡化后的直方图
cv.imshow("fourth", b1)#均衡化后的累计直方图
cv.imshow('img2',equ)
cv.waitKey()
cv.destroyAllWindows()

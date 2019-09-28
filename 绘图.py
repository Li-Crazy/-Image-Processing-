import matplotlib.pyplot as plt
import numpy as np
import pygal

# 构建数据
X = [0,1/7,2/7,3/7,4/7,5/7,6/7,1]
Y1 = {0:0.354, 1/7:0.251, 2/7:0.129, 3/7:0.090, 4/7:0.068, 5/7:0.050, 6/7:0.037, 1:0.020}
Y2 = {0:0, 1/7:0, 2/7:0.354, 3/7:0, 4/7:0.251, 5/7:0.129, 6/7:0.159, 1:0.106}


# 绘图
view = pygal.Bar()
view.title = "原图像直方图"
view.x_labels = X
view.add("Pr(rk)",Y1)
view.render_in_browser()

view1 = pygal.Bar()
view1.title = "新的直方图"
view1.x_labels = X
view1.add("Ps(sl)",Y2)
view1.render_in_browser()
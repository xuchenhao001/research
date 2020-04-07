# -*- coding:utf-8 -*-
# !/usr/bin/python
import numpy as np
from matplotlib import pyplot as pl

# 解决matplotlib显示中文乱码问题
# pl.rcParams['font.sans-serif'] = ['SimHei']
# pl.rcParams['axes.unicode_minus'] = False
fig, ax = pl.subplots()


# 计算基尼系数
def gini():
    # 计算数组累计值,从 0 开始
    # wealths = [1.5, 2, 3.5, 10, 4.2, 2.1, 1.1, 2.2, 3.1, 5.1, 9.5, 9.7, 1.7, 2.3, 3.8, 1.7, 2.3, 5, 4.7, 2.3, 4.3, 12]
    received = [1,1,1,8,0.5,4.5]
    cum_wealths = np.cumsum(sorted(np.append(received, 0)))
    # 取最后一个，也就是原数组的和
    sum_wealths = cum_wealths[-1]
    # 人数的累积占比
    xarray = np.array(range(0, len(cum_wealths))) / np.float(len(cum_wealths) - 1)

    # 均衡收入曲线
    upper = xarray
    # 收入累积占比
    yarray = cum_wealths / sum_wealths
    # 绘制基尼系数对应的洛伦兹曲线
    ax.plot(xarray, yarray)
    ax.plot(xarray, upper)
    ax.set_xlabel('population')
    ax.set_ylabel('received')
    pl.show()
    # 计算曲线下面积的通用方法
    B = np.trapz(yarray, x=xarray)
    # 总面积 0.5
    A = 0.5 - B
    G = A / (A + B)
    return G


a = gini()
print(a)

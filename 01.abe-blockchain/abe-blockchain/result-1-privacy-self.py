# -*- coding:utf-8 -*-
# !/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

x = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

ps2 = [0.25, 0.214285714, 0.25, 0.222222222, 0.25, 0.227272727, 0.25, 0.230769231, 0.25, 0.233333333, 0.25, 0.235294118, 0.25, 0.236842105, 0.25]
ps3 = [0.166667, 0.142857, 0.166667, 0.148148, 0.166667, 0.151515, 0.166667, 0.153846, 0.166667, 0.155556, 0.166667, 0.156863, 0.166667, 0.157895, 0.166667]
ps4 = [0.125000, 0.107143, 0.125000, 0.111111, 0.125000, 0.113636, 0.125000, 0.115385, 0.125000, 0.116667, 0.125000, 0.117647, 0.125000, 0.118421, 0.125000]
ps5 = [0.100000, 0.085714, 0.100000, 0.088889, 0.100000, 0.090909, 0.100000, 0.092308, 0.100000, 0.093333, 0.100000, 0.094118, 0.100000, 0.094737, 0.100000]
ps6 = [0.083333, 0.071429, 0.083333, 0.074074, 0.083333, 0.075758, 0.083333, 0.076923, 0.083333, 0.077778, 0.083333, 0.078431, 0.083333, 0.078947, 0.083333]

fig, axes = plt.subplots()

csfont = {'fontname': 'Times New Roman'}
legendFont = font_manager.FontProperties(family='Times New Roman')
xylabelFont = font_manager.FontProperties(family='Times New Roman')
csXYLabelFont = {'fontproperties': xylabelFont}
axesFont = font_manager.FontProperties(family='Times New Roman')
csAxesFont = {'fontproperties': axesFont}

axes.plot(x, ps2, marker="o", label="φ = 2")
axes.plot(x, ps3, marker="^", label="φ = 3")
axes.plot(x, ps4, marker="s", label="φ = 4")
axes.plot(x, ps5, marker="*", label="φ = 5")

plt.xlabel("The number of organizations participated in blockchain", fontsize=16, **csfont)
plt.ylabel("The proportion of staffs can decrypt transaction", fontsize=16, **csfont)
plt.xticks(**csAxesFont)
plt.yticks(**csAxesFont)
plt.legend(prop=legendFont)
plt.grid()
plt.show()

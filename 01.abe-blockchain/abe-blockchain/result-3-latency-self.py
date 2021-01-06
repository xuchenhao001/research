# -*- coding:utf-8 -*-
# !/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

x = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# v2 here
ps = [1.081521676, 1.08178736, 1.083384664, 1.084784245, 1.085623646, 1.08763931, 1.087209926, 1.088188603, 1.090169542, 1.094597521, 1.094860847, 1.09555953, 1.099339802, 1.099048355, 1.098870022]
ps2 = [1.081185064, 1.084572289, 1.085479102, 1.086420413, 1.088318756, 1.088925079, 1.090615134, 1.09130214, 1.092735288, 1.095033979, 1.095140377, 1.096485741, 1.098599536, 1.10051413, 1.100644594]
ps3 = [1.080131074, 1.08299553, 1.084450543, 1.086823239, 1.088556884, 1.088714973, 1.089284096, 1.091398635, 1.093526412, 1.093835748, 1.096478133, 1.097221634, 1.10164972, 1.098747686, 1.100646236]

fig, axes = plt.subplots()

csfont = {'fontname': 'Times New Roman'}
legendFont = font_manager.FontProperties(family='Times New Roman')
xylabelFont = font_manager.FontProperties(family='Times New Roman')
csXYLabelFont = {'fontproperties': xylabelFont}
axesFont = font_manager.FontProperties(family='Times New Roman')
csAxesFont = {'fontproperties': axesFont}

axes.plot(x, ps, marker="o", label="80bit")
axes.plot(x, ps2, marker="^", label="112bit")
axes.plot(x, ps3, marker="s", label="128bit")

plt.xlabel("The number of organizations participated in blockchain", fontsize=16, **csfont)
plt.ylabel("Latency (s)", fontsize=16, **csfont)
plt.xticks(**csAxesFont)
plt.yticks(**csAxesFont)
plt.legend(prop=legendFont)
plt.tight_layout(pad=1.08)
plt.grid()
plt.show()

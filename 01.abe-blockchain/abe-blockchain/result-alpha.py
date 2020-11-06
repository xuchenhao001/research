# -*- coding:utf-8 -*-
# !/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

x = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

alpha = [6.372902604, 6.583900536, 7.749924657, 9.183869872, 9.558664628, 11.24971311, 12.14302386, 13.39397196, 13.68034982, 15.06902084, 16.09358803, 17.01503801, 18.2038325, 18.69833776, 20.34125205]
round_alpha = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

fig, axes = plt.subplots()

csfont = {'fontname': 'Times New Roman'}
legendFont = font_manager.FontProperties(family='Times New Roman')
xylabelFont = font_manager.FontProperties(family='Times New Roman')
csXYLabelFont = {'fontproperties': xylabelFont}
axesFont = font_manager.FontProperties(family='Times New Roman')
csAxesFont = {'fontproperties': axesFont}

# axes.plot(x, alpha, marker="o", label="α")
width = 0.5
axes.bar(x, height=alpha, width=width, label="α")
axes.plot(x, round_alpha, marker="^", label="Round α", color="#ff7f0e")

plt.xlabel("The number of organizations participate in blockchain", fontsize=16, **csfont)
plt.ylabel("The value of α", fontsize=16, **csfont)
plt.xticks(**csAxesFont)
plt.yticks(**csAxesFont)
plt.legend(prop=legendFont)
plt.grid()
plt.show()

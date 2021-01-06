# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

x = [20, 50, 100, 150, 200]
pow = [124.611792, 119.930167, 129.225645, 139.737972, 145.820153]
pos = [90.899976, 92.468626, 101.597937, 108.22578, 115.567716]
cma = [41.519605, 42.374302, 42.024125, 46.744841, 46.220964]

fig, axes = plt.subplots()

# legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=20)
# xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=22)
# legendFont = font_manager.FontProperties(family='Times New Roman')
xylabelFont = font_manager.FontProperties(family='Times New Roman', size=16)
csXYLabelFont = {'fontproperties': xylabelFont}
# axesFont = font_manager.FontProperties(family='Times New Roman', size=20)
# csAxesFont = {'fontproperties': axesFont}

width = 10  # the width of the bars
axes.bar([p + width for p in x], height=cma, width=width, label="CMA")
axes.bar([p - width for p in x], height=pow, width=width, label="PoW")
axes.bar(x, height=pos, width=width, label="PoS")
axes.set_xlabel("Number of participants", **csXYLabelFont)
axes.set_ylabel("Total time consumption (s)", **csXYLabelFont)

# plt.xticks(**csAxesFont)
# plt.yticks(**csAxesFont)
# plt.legend(prop=legendFont, loc='upper left')
plt.legend()
plt.grid()
plt.show()

# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

x = [10, 20, 30, 40, 50]
pow = [50.78094, 74.087858, 91.982859, 114.842697, 129.989067]
pos = [44.274122, 57.663999, 72.052244, 84.785868, 98.419618]
cma = [45.458099, 44.992936, 44.597361, 44.758357, 44.223097]

fig, axes = plt.subplots()

# legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=20)
# xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=22)
# legendFont = font_manager.FontProperties(family='Times New Roman')
xylabelFont = font_manager.FontProperties(family='Times New Roman', size=16)
csXYLabelFont = {'fontproperties': xylabelFont}
# axesFont = font_manager.FontProperties(family='Times New Roman', size=20)
# csAxesFont = {'fontproperties': axesFont}

width = 3  # the width of the bars
axes.bar([p + width for p in x], height=cma, width=width, label="CMA")
axes.bar([p - width for p in x], height=pow, width=width, label="PoW")
axes.bar(x, height=pos, width=width, label="PoS")
axes.set_xlabel("Incoming transaction speed (tx/s)", **csXYLabelFont)
axes.set_ylabel("Total time consumption (s)", **csXYLabelFont)

# plt.xticks(**csAxesFont)
# plt.yticks(**csAxesFont)
# plt.legend(prop=legendFont, loc='upper left')
plt.legend()
plt.grid()
plt.show()

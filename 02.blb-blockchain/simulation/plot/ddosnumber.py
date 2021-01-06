# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

# x = [0, 10, 20, 40, 60, 80, 100]
# pow = [100.938952, 102.539916, 102.722243, 104.893434, 109.613633, 123.115097, 136.778802]
# pos = [68.083165, 67.729969, 69.602602, 70.663737, 71.866389, 71.746657, 77.894401]
# cma = [14.021015, 12.656469, 12.998163, 13.845206, 13.496134, 13.469494, 14.308062]

x = [0, 20, 40, 60, 80, 100]
pow = [130.749802, 138.559137, 140.213036, 146.15417, 153.887892, 156.480009]
pos = [98.435802, 100.091204, 100.248583, 96.235801, 103.746948, 102.199121]
cma = [43.53462, 43.673138, 43.641557, 44.274799, 44.668429, 44.290468]

fig, axes = plt.subplots()

# legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=20)
# xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=22)
# legendFont = font_manager.FontProperties(family='Times New Roman')
xylabelFont = font_manager.FontProperties(family='Times New Roman', size=16)
csXYLabelFont = {'fontproperties': xylabelFont}
# axesFont = font_manager.FontProperties(family='Times New Roman', size=20)
# csAxesFont = {'fontproperties': axesFont}

axes.plot(x, cma, marker="o", label="CMA")
axes.plot(x, pow, marker="s", label="PoW")
axes.plot(x, pos, marker="+", label=r"PoS")
# width = 6  # the width of the bars
# axes.bar([p + width for p in x], height=cma, width=width, label="CMA")
# axes.bar([p - width for p in x], height=pow, width=width, label="PoW")
# axes.bar(x, height=pos, width=width, label="PoS")
axes.set_xlabel("Number of participants under attack", **csXYLabelFont)
axes.set_ylabel("Total time consumption (s)", **csXYLabelFont)

# plt.xticks(**csAxesFont)
# plt.yticks(**csAxesFont)
# plt.legend(prop=legendFont, loc='upper left')
plt.legend()
plt.grid()
plt.show()

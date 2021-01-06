# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

x = [10, 20, 30, 40, 50, 60]
pow = [47.73158, 93.114892, 140.004355, 184.375631, 236.511841, 289.943089]
pos = [33.319528, 62.582494, 100.429156, 134.78289, 166.866376, 199.652467]
cma = [14.95417, 29.684793, 44.017046, 58.521419, 73.675574, 87.902069]

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
# width = 3  # the width of the bars
# axes.bar([p + width for p in x], height=cma, width=width, label="CMA")
# axes.bar([p - width for p in x], height=pow, width=width, label="PoW")
# axes.bar(x, height=pos, width=width, label="PoS")

axes.set_xlabel("Total incoming transaction duration (s)", **csXYLabelFont)
axes.set_ylabel("Total time consumption (s)", **csXYLabelFont)

# plt.xticks(**csAxesFont)
# plt.yticks(**csAxesFont)
# plt.legend(prop=legendFont, loc='upper left')
plt.legend()
plt.grid()
plt.show()

# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

x = [4, 6, 8, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
pow = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
pos_min = [0.044034128, 0.058485399, 0.104859123, 0.054605023, 0.041428914, 0.039285107, 0.024834101, 0.031275523, 0.055713088, 0.036759854, 0.030449251, 0.045421642, 0.029625322, 0.025153839, 0.043130023, 0.034092331, 0.034734866, 0.032748474, 0.045159618, 0.034878054, 0.029717622, 0.03318737, 0.028235354]
pos_max = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
cma = [0.014773351, 0.0001, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

fig, axes = plt.subplots()

# legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=20)
xylabelFont = font_manager.FontProperties(family='Times New Roman', style='normal', size=22)
# legendFont = font_manager.FontProperties(family='Times New Roman', style='normal')
# xylabelFont = font_manager.FontProperties(family='Times New Roman', size=16)
csXYLabelFont = {'fontproperties': xylabelFont}
# axesFont = font_manager.FontProperties(family='Times New Roman', size=20)
# axesFont = font_manager.FontProperties(family='Times New Roman')
# csAxesFont = {'fontproperties': axesFont}

axes.plot(x, cma, marker="o", label="CMA")
axes.plot(x, pow, marker="s", label="PoW")
axes.plot(x, pos_min, marker="^", label=r"PoS MIN")
axes.plot(x, pos_max, marker="D", label=r"PoS MAX")

axes.set_xlabel("The number of participants (α = 0.5 * η)", **csXYLabelFont)
axes.set_ylabel("Attacker's probability of success", **csXYLabelFont)

# plt.xticks(**csAxesFont)
# plt.yticks(**csAxesFont)
# plt.legend(prop=legendFont, loc='upper left')
plt.legend()
plt.grid()
plt.show()

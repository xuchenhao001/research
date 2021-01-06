# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

x = [8, 12, 20, 32, 40, 52, 60, 72, 80, 92, 100, 112, 120, 132, 140, 152, 160, 172, 180, 192, 200]
cma = [2.77E-05, 7.03E-09, 3.33E-16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pow = [0.078030536, 0.078030536, 0.078030536, 0.078030536, 0.078030536, 0.078030536, 0.078030536, 0.078030536, 0.078030536, 0.078030536, 0.078030536, 0.078030536, 0.078030536, 0.078030536, 0.078030536, 0.078030536, 0.078030536, 0.078030536, 0.078030536, 0.078030536, 0.078030536]
pos_min = [0.000720858, 0.000210748, 0.000238688, 5.5385E-05, 0.000259812, 8.47487E-05, 0.000120609, 6.84083E-05, 0.000186845, 0.00021549, 0.000143576, 0.000134969, 0.000156916, 0.000151035, 0.00017229, 9.91347E-05, 0.000104763, 0.00020973, 0.000117013, 8.55196E-05, 0.000114401]
pos_max = [1, 1, 1, 0.745568004, 1, 1, 1, 1, 0.83242641, 1, 1, 0.970648855, 0.965561847, 0.893343674, 1, 1, 1, 0.991691574, 1, 1, 0.96416829]

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

axes.set_xlabel("The number of participants (α = 0.25 * η)", **csXYLabelFont)
axes.set_ylabel("Attacker's probability of success", **csXYLabelFont)

# plt.xticks(**csAxesFont)
# plt.yticks(**csAxesFont)
# plt.legend(prop=legendFont, loc='upper left')
plt.legend()
plt.grid()
plt.show()

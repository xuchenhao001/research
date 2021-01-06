# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
cma = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pow = [1.03E-08, 1.66E-07, 8.43E-07, 2.68E-06, 6.58E-06, 1.37E-05, 2.55E-05, 4.38E-05, 7.05E-05, 0.000108016, 0.00181433, 0.009576559, 0.031279531, 0.078030536, 0.162926427, 0.298223016, 0.49040418, 0.733187347, 1]
pos_min = [3.21965E-15, 9.62933E-14, 9.79624E-13, 6.45117E-12, 2.99762E-11, 1.11745E-10, 3.49847E-10, 8.8759E-10, 1.91185E-09, 3.69685E-09, 2.92282E-07, 5.62657E-06, 4.88804E-05, 0.000253014, 0.000991001, 0.003161242, 0.008631286, 0.021550136, 0.050222613]
pos_max = [3.30E-06, 4.08E-05, 9.71E-05, 0.000314103, 0.000747974, 0.001341219, 0.002435356, 0.003398903, 0.005749947, 0.008445262, 0.070242013, 0.366562859, 0.665590273, 1, 1, 1, 1, 1, 1]

fig, axes = plt.subplots()

# legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=20)
# xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=22)
# legendFont = font_manager.FontProperties(family='Times New Roman', style='normal')
xylabelFont = font_manager.FontProperties(family='Times New Roman', size=16)
csXYLabelFont = {'fontproperties': xylabelFont}
# axesFont = font_manager.FontProperties(family='Times New Roman', size=20)
# axesFont = font_manager.FontProperties(family='Times New Roman')
# csAxesFont = {'fontproperties': axesFont}

axes.plot(x, cma, marker="o", label="CMA")
axes.plot(x, pow, marker="s", label="PoW")
axes.plot(x, pos_min, marker="^", label=r"PoS MIN")
axes.plot(x, pos_max, marker="D", label=r"PoS MAX")
# width = 3  # the width of the bars
# axes.bar([p + width for p in x], height=cma, width=width, label="CMA")
# axes.bar([p - width for p in x], height=pow, width=width, label="PoW")
# axes.bar(x, height=pos, width=width, label="PoS")

axes.set_xlabel("The number of nodes controlled by the attacker", **csXYLabelFont)
axes.set_ylabel("Attacker's probability of success", **csXYLabelFont)

# plt.xticks(**csAxesFont)
# plt.yticks(**csAxesFont)
# plt.legend(prop=legendFont, loc='upper left')
plt.legend()
plt.grid()
plt.show()

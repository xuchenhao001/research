# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

x = [1, 2, 3, 4, 5, 6, 7]
z1 = [1, 0.201550401, 0.043241166, 0.009803102, 2.28E-03, 5.31E-04, 1.24E-04]
z2 = [1, 0.123304132, 0.013444272, 0.001506364, 1.71E-04, 1.95E-05, 2.20E-06]
z3 = [1, 0.076444965, 0.004253695, 0.000235928, 1.31E-05, 7.29E-07, 3.98E-08]
z4 = [1, 0.047812168, 0.001360734, 3.74E-05, 1.02E-06, 2.76E-08, 7.31E-10]
z5 = [1, 0.030084056, 0.000438464, 5.97E-06, 8.00E-08, 1.05E-09, 1.35E-11]
z6 = [1, 0.019011117, 0.000142003, 9.59E-07, 6.30E-09, 4.04E-11, 2.51E-13]

fig, axes = plt.subplots()

# legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=20)
# xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=22)
# legendFont = font_manager.FontProperties(family='Times New Roman', style='normal')
xylabelFont = font_manager.FontProperties(family='Times New Roman', size=16)
csXYLabelFont = {'fontproperties': xylabelFont}
# axesFont = font_manager.FontProperties(family='Times New Roman', size=20)
# axesFont = font_manager.FontProperties(family='Times New Roman')
# csAxesFont = {'fontproperties': axesFont}

axes.plot(x, z1, marker="o", label="z=1")
axes.plot(x, z2, marker="s", label="z=2")
axes.plot(x, z3, marker="^", label="z=3")
axes.plot(x, z4, marker="D", label="z=4")
axes.plot(x, z5, marker="1", label="z=5")
axes.plot(x, z6, marker="x", label="z=6")

axes.set_xlabel("The number of committee members", **csXYLabelFont)
axes.set_ylabel("Attacker's probability of success", **csXYLabelFont)

# plt.xticks(**csAxesFont)
# plt.yticks(**csAxesFont)
# plt.legend(prop=legendFont, loc='upper left')
plt.legend()
plt.grid()
plt.show()

# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

x = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]
cma = [1.81E-03, 1.26E-08, 6.04E-14, 0, 0, 1.11E-16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pow = [0.00181433, 0.00181433, 0.00181433, 0.00181433, 0.00181433, 0.00181433, 0.00181433, 0.00181433, 0.00181433, 0.00181433, 0.00181433, 0.00181433, 0.00181433, 0.00181433, 0.00181433, 0.00181433, 0.00181433, 0.00181433, 0.00181433, 0.00181433]
pos_min = [1.71369E-07, 1.50567E-07, 1.18563E-07, 9.28125E-08, 5.43505E-07, 1.66108E-07, 1.1082E-07, 8.78001E-08, 1.34779E-07, 1.16977E-07, 6.00458E-08, 2.99466E-08, 3.51792E-08, 1.93022E-07, 8.07398E-08, 3.91085E-07, 6.40983E-08, 1.68062E-07, 9.24205E-08, 1.19346E-07]
pos_max = [0.062179807, 0.031964339, 0.068733723, 0.062590604, 0.048649673, 0.109818894, 0.093231417, 0.098593926, 0.059608734, 0.083136403, 0.086746997, 0.07651431, 0.062647708, 0.058852327, 0.116008609, 0.084398524, 0.065127185, 0.077944589, 0.068409233, 0.108559124]

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

axes.set_xlabel("The number of participants (α = 0.1 * η)", **csXYLabelFont)
axes.set_ylabel("Attacker's probability of success", **csXYLabelFont)

# plt.xticks(**csAxesFont)
# plt.yticks(**csAxesFont)
# plt.legend(prop=legendFont, loc='upper left')
plt.legend()
plt.grid()
plt.show()

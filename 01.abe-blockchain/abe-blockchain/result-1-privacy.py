# -*- coding:utf-8 -*-
# !/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

x = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

ps = [300.000000, 300.000000, 400.000000, 400.000000, 500.000000, 500.000000, 600.000000, 600.000000, 700.000000,
      700.000000, 800.000000, 800.000000, 900.000000, 900.000000, 1000.000000]
fixa = [300.000000, 331.226854, 475.682846, 503.968420, 659.753955, 685.175492, 848.528137, 871.453714, 1040.196002,
        1061.001597, 1233.768660, 1252.777953, 1428.660947, 1446.140208, 1624.504793]
csl = [1200.000000, 1400.000000, 1600.000000, 1800.000000, 2000.000000, 2200.000000, 2400.000000, 2600.000000,
       2800.000000, 3000.000000, 3200.000000, 3400.000000, 3600.000000, 3800.000000, 4000.000000]
# pels3 = [600, 600, 600, 600, 600, 600, 600, 600, 600, 600, 600, 600, 600, 600, 600]
# pels4 = [800, 800, 800, 800, 800, 800, 800, 800, 800, 800, 800, 800, 800, 800, 800]
pels5 = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]


fig, axes = plt.subplots()

csfont = {'fontname': 'Times New Roman'}
legendFont = font_manager.FontProperties(family='Times New Roman')
xylabelFont = font_manager.FontProperties(family='Times New Roman')
csXYLabelFont = {'fontproperties': xylabelFont}
axesFont = font_manager.FontProperties(family='Times New Roman')
csAxesFont = {'fontproperties': axesFont}

axes.plot(x, ps, marker="o", label="MA-ABE")
axes.plot(x, fixa, marker="^", label="FIXA")
axes.plot(x, csl, marker="s", label="CSL")
# axes.plot(x, pels3, marker="x", label="PEL s3")
# axes.plot(x, pels4, marker="D", label="PEL s4")
axes.plot(x, pels5, marker="*", label="PEL")

plt.xlabel("η", fontsize=16, **csfont)
plt.ylabel("Privacy", fontsize=16, **csfont)
plt.xticks(**csAxesFont)
plt.yticks(**csAxesFont)
plt.legend(prop=legendFont)
plt.grid()
plt.show()

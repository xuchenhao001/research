# -*- coding:utf-8 -*-
# !/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

x = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
ps = [88.0078125, 103.359375, 118.875, 134.578125, 150.5078125, 166.5898438, 182.859375, 199.3671875, 216.015625,
      232.8515625, 249.9375, 267.1523438, 284.625, 302.21875, 320]
# fixa = [88.0078125, 102.6757813, 117.34375, 132.0117188, 146.6796875, 161.3476563, 176.015625, 190.6835938,
#         205.3515625, 220.0195313, 234.6875, 249.3554688, 264.0234375, 278.6914063, 293.359375]
fixa = [111, 127, 143, 159, 175, 191, 207, 223, 239, 255, 271, 287, 303, 319, 335]
csl = [60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
pels3 = [249.0117188, 290.5136719, 332.015625, 373.5175781, 415.0195313, 456.5214844, 498.0234375, 539.5253906,
         581.0273438, 622.5292969, 664.03125, 705.5332031, 747.0351563, 788.5371094, 830.0390625]
pels4 = [332.015625, 387.3515625, 442.6875, 498.0234375, 553.359375, 608.6953125, 664.03125, 719.3671875, 774.703125,
         830.0390625, 885.375, 940.7109375, 996.046875, 1051.382813, 1106.71875]
pels5 = [415.0195313, 484.1894531, 553.359375, 622.5292969, 691.6992188, 760.8691406, 830.0390625, 899.2089844,
         968.3789063, 1037.548828, 1106.71875, 1175.888672, 1245.058594, 1314.228516, 1383.398438]


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

plt.xlabel("The number of organizations participated in blockchain", fontsize=16, **csfont)
plt.ylabel("Storage Consumption (KB)", fontsize=16, **csfont)
plt.xticks(**csAxesFont)
plt.yticks(**csAxesFont)
plt.legend(prop=legendFont)
plt.grid()
plt.show()

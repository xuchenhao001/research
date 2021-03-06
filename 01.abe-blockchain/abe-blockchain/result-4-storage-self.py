# -*- coding:utf-8 -*-
# !/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

x = [6, 7, 8, 9, 10]
# ps =  [88.0078125, 103.359375, 118.875, 134.578125, 150.5078125, 166.5898438, 182.859375, 199.3671875, 216.015625, 232.8515625, 249.9375, 267.1523438, 284.625, 302.21875, 320]
# ps2 = [88.2421875, 103.6328125, 119.1875, 134.9296875, 150.8984375, 167.0195313, 183.328125, 199.875, 216.5625, 233.4375, 250.5625, 267.8164063, 285.328125, 302.9609375, 320.78125]
# ps3 = [88.5, 103.9335938, 119.53125, 135.3164063, 151.328125, 167.4921875, 183.84375, 200.4335938, 217.1640625, 234.0820313, 251.25, 268.546875, 286.1015625, 303.7773438, 321.640625]
ps = [88.0078125, 103.359375, 118.875, 134.578125, 150.5078125]
ps2 = [88.2421875, 103.6328125, 119.1875, 134.9296875, 150.8984375]
ps3 = [88.5, 103.9335938, 119.53125, 135.3164063, 151.328125]

fig, axes = plt.subplots()

csfont = {'fontname': 'Times New Roman'}
legendFont = font_manager.FontProperties(family='Times New Roman')
xylabelFont = font_manager.FontProperties(family='Times New Roman')
csXYLabelFont = {'fontproperties': xylabelFont}
axesFont = font_manager.FontProperties(family='Times New Roman')
csAxesFont = {'fontproperties': axesFont}

# axes.plot(x, ps, marker="o", label="80bit")
# axes.plot(x, ps2, marker="^", label="112bit")
# axes.plot(x, ps3, marker="s", label="128bit")

width = 0.2  # the width of the bars
axes.bar([p - width for p in x], height=ps, width=width, label="80bit")
axes.bar(x, height=ps2, width=width, label="112bit")
axes.bar([p + width for p in x], height=ps3, width=width, label="128bit")

plt.xlabel("The number of organizations participated in blockchain", fontsize=16, **csfont)
plt.ylabel("Storage Consumption (KB)", fontsize=16, **csfont)
plt.xticks(**csAxesFont)
plt.yticks(**csAxesFont)
plt.legend(prop=legendFont)
plt.tight_layout(pad=1.08)
plt.grid()
plt.show()

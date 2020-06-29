# -*- coding:utf-8 -*-
# !/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

x = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

ps = [0.509004, 0.582774, 0.519957, 0.577384, 0.534648, 0.580660, 0.551427, 0.589617, 0.570708, 0.602594, 0.591311,
      0.618432, 0.613153, 0.636181, 0.635186]
# fixa = [0.509004, 0.582774, 0.519957, 0.577384, 0.534648, 0.580660, 0.551427, 0.589617, 0.570708, 0.602594, 0.591311,
#         0.618432, 0.613153, 0.636181, 0.635186]
fixa = [0.519004, 0.592774, 0.529957, 0.587384, 0.544648, 0.590660, 0.561427, 0.599617, 0.580708, 0.612594, 0.601311,
        0.628432, 0.623153, 0.646181, 0.645186]
csl = [0.031076, 0.041439, 0.053385, 0.066648, 0.081317, 0.097175, 0.114236, 0.132296, 0.151318, 0.171098, 0.191562,
       0.212509, 0.233842, 0.255364, 0.276976]
pels1 = [0.833333, 0.857143, 0.875000, 0.888889, 0.900000, 0.909091, 0.916667, 0.923077, 0.928571, 0.933333, 0.937500, 0.941176, 0.944444, 0.947368, 0.950000]
pels2 = [0.668333, 0.714286, 0.751250, 0.777778, 0.801000, 0.818182, 0.834167, 0.846154, 0.857857, 0.866667, 0.875625, 0.882353, 0.889444, 0.894737, 0.900500]
pels3 = [0.502230, 0.575212, 0.626672, 0.669610, 0.701338, 0.729681, 0.751115, 0.771268, 0.786670, 0.801766, 0.813336, 0.825087, 0.834077, 0.843499, 0.850669]
pels4 = [0.343232, 0.434285, 0.507424, 0.559999, 0.605939, 0.640000, 0.671616, 0.695384, 0.718528, 0.736000, 0.753712, 0.767059, 0.781077, 0.791579, 0.802970]
pels5 = [0.181289, 0.301482, 0.385967, 0.456708, 0.508773, 0.555489, 0.590644, 0.623875, 0.649124, 0.674025, 0.692983, 0.712375, 0.727096, 0.742651, 0.754387]


fig, axes = plt.subplots()

csfont = {'fontname': 'Times New Roman'}
legendFont = font_manager.FontProperties(family='Times New Roman')
xylabelFont = font_manager.FontProperties(family='Times New Roman')
csXYLabelFont = {'fontproperties': xylabelFont}
axesFont = font_manager.FontProperties(family='Times New Roman')
csAxesFont = {'fontproperties': axesFont}

axes.plot(x, ps, marker="o", label="MA-ABE")
axes.plot(x, fixa, marker="^", label="FIXA", linestyle="--")
# axes.plot(x, csl, marker="s", label="CSL")
# axes.plot(x, pels1, marker="x", label="PEL s1")
axes.plot(x, pels2, marker="x", label="PEL")
# axes.plot(x, pels3, marker="x", label="PEL s3")
# axes.plot(x, pels4, marker="D", label="PEL s4")
# axes.plot(x, pels5, marker="*", label="PEL s5")

plt.xlabel("η", fontsize=16, **csfont)
plt.ylabel("Decentralization", fontsize=16, **csfont)
plt.xticks(**csAxesFont)
plt.yticks(**csAxesFont)
plt.legend(prop=legendFont)
plt.grid()
plt.show()

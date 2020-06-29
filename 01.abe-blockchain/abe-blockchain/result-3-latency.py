# -*- coding:utf-8 -*-
# !/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

x = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# ps = [0.081521676, 0.08178736, 0.083384664, 0.084784245, 0.085623646, 0.08763931, 0.087209926, 0.088188603,
#       0.090169542, 0.094597521, 0.094860847, 0.09555953, 0.099339802, 0.099048355, 0.098870022]
# at last we choose fixa 18
# fixa = [0.100026782, 0.097548611, 0.097810583, 0.097699158, 0.097908525, 0.098557074, 0.100144241, 0.103615303,
#         0.100313022, 0.100117276, 0.100362833, 0.099821544, 0.102147305, 0.10267982, 0.100647676]
# csl = [0.050000, 0.050000, 0.050000, 0.050000, 0.050000, 0.050000, 0.050000, 0.050000, 0.050000, 0.050000, 0.050000,
#        0.050000, 0.050000, 0.050000, 0.050000]
# pels3 = [0.088120725, 0.085920768, 0.086541936, 0.086011124, 0.086089923, 0.086360061, 0.091403699, 0.085911949,
#          0.087148738, 0.086225941, 0.086144145, 0.087475481, 0.089222457, 0.087650597, 0.091908267]
# pels4 = [0.096092753, 0.097637227, 0.095897806, 0.096166146, 0.096262872, 0.097176178, 0.096600981, 0.096820166,
#          0.096055059, 0.096943905, 0.095813119, 0.100646718, 0.097012303, 0.096771512, 0.101183639]
# pels5 = [0.104557583, 0.105303349, 0.104967299, 0.107792332, 0.106249318, 0.104748106, 0.105489886, 0.105444796,
#          0.108379166, 0.105057714, 0.105744848, 0.109217343, 0.105896754, 0.104447165, 0.106449521]


# v2 here
ps = [1.081521676, 1.08178736, 1.083384664, 1.084784245, 1.085623646, 1.08763931, 1.087209926, 1.088188603, 1.090169542, 1.094597521, 1.094860847, 1.09555953, 1.099339802, 1.099048355, 1.098870022]
fixa = [1.100026782, 1.097548611, 1.097810583, 1.097699158, 1.097908525, 1.098557074, 1.100144241, 1.103615303, 1.100313022, 1.100117276, 1.100362833, 1.099821544, 1.102147305, 1.10267982, 1.100647676]
csl = [1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05]
pels5 = [1.104557583, 1.105303349, 1.104967299, 1.107792332, 1.106249318, 1.104748106, 1.105489886, 1.105444796, 1.108379166, 1.105057714, 1.105744848, 1.109217343, 1.105896754, 1.104447165, 1.106449521]

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
plt.ylabel("Latency (s)", fontsize=16, **csfont)
plt.xticks(**csAxesFont)
plt.yticks(**csAxesFont)
plt.legend(prop=legendFont)
plt.grid()
plt.show()

# -*- coding: UTF-8 -*-

# For ubuntu env error: findfont: Font family ['Times New Roman'] not found. Falling back to DejaVu Sans.
# ```bash
# sudo apt-get install msttcorefonts
# rm -rf ~/.cache/matplotlib
# ```

import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
     32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
local_train = [5.40, 94.75, 96.60, 97.25, 97.50, 97.75, 97.85, 98.20, 98.20, 98.20, 98.35, 98.35, 98.35, 98.40, 98.40, 98.45, 98.05, 98.40, 98.50, 98.40, 98.30, 98.40, 98.45, 98.50, 98.50, 98.35, 98.30, 98.45, 98.50, 98.35, 98.25, 98.55, 98.50, 98.65, 98.10, 98.50, 98.55, 98.35, 98.60, 98.45, 98.45, 98.55, 98.40, 98.55, 98.65, 98.65, 98.55, 98.55, 98.50, 98.50]
fed_avg = [43.95, 72.70, 79.00, 81.35, 84.90, 86.40, 88.85, 89.85, 91.05, 91.85, 92.00, 92.55, 92.90, 93.15, 93.55, 93.90, 93.65, 94.25, 94.20, 93.95, 94.20, 94.40, 94.75, 94.80, 95.05, 94.80, 95.00, 95.30, 95.60, 95.70, 95.20, 95.85, 96.20, 96.20, 95.95, 96.25, 96.55, 96.55, 96.40, 96.50, 96.65, 96.35, 96.60, 97.00, 96.95, 97.10, 96.90, 96.80, 96.95, 96.90]
scei = [93.65, 96.50, 97.40, 97.55, 97.75, 98.25, 98.20, 98.05, 97.85, 98.45, 98.40, 98.25, 98.55, 98.45, 98.70, 98.55, 98.45, 98.60, 98.65, 98.85, 98.85, 98.60, 98.75, 98.90, 98.75, 98.95, 98.85, 98.95, 98.85, 98.80, 98.90, 98.90, 98.75, 98.75, 98.75, 98.80, 98.80, 98.75, 98.95, 98.75, 99.00, 98.65, 98.90, 99.00, 98.85, 99.05, 99.05, 99.00, 99.15, 98.85]
a025 = [73.30, 82.60, 88.00, 90.95, 92.40, 93.35, 94.95, 94.35, 96.00, 96.00, 96.15, 96.35, 96.80, 97.00, 96.85, 97.40, 97.20, 97.55, 97.85, 97.85, 97.85, 97.65, 97.80, 97.90, 97.85, 98.05, 98.00, 97.90, 98.00, 98.15, 98.10, 97.95, 98.00, 98.25, 98.30, 98.40, 98.15, 98.50, 98.25, 98.40, 98.40, 98.60, 98.20, 98.55, 98.25, 98.60, 98.40, 98.35, 98.50, 98.40]
a05 = [93.40, 95.60, 96.30, 96.60, 96.95, 97.20, 97.20, 97.85, 98.00, 97.65, 98.00, 98.20, 98.30, 98.20, 98.45, 98.40, 98.70, 98.40, 99.00, 98.90, 98.80, 98.65, 98.60, 98.90, 98.95, 98.65, 98.90, 98.65, 98.70, 98.90, 98.80, 98.75, 98.95, 98.95, 98.90, 99.05, 98.90, 98.55, 98.55, 98.95, 99.00, 98.80, 99.00, 99.05, 98.90, 98.95, 98.90, 98.90, 98.75, 98.95]
a075 = [94.50, 97.05, 97.35, 97.50, 97.50, 97.80, 97.85, 98.00, 98.10, 97.90, 98.65, 98.60, 98.25, 98.40, 98.30, 98.30, 98.35, 98.70, 98.60, 98.30, 98.65, 98.75, 98.75, 98.80, 98.55, 98.65, 98.60, 98.70, 98.70, 98.75, 98.80, 98.65, 98.70, 98.80, 98.70, 98.70, 98.75, 98.65, 98.65, 98.95, 98.85, 98.85, 98.70, 98.80, 99.00, 98.85, 98.85, 99.15, 98.90, 99.05]

fig, axes = plt.subplots()

legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=15)
xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=17)
csXYLabelFont = {'fontproperties': xylabelFont}

axes.plot(x, scei, label="negotiated α (0.5-0.8)", linewidth=3)
axes.plot(x, fed_avg, label="α=0.0 (i.e. FedAvg)", linestyle='--', alpha=0.5)
axes.plot(x, a025, label="α=0.25", linestyle='--', alpha=0.5)
axes.plot(x, a05, label="α=0.5", linestyle='--', alpha=0.5)
axes.plot(x, a075, label="α=0.75", linestyle='--', alpha=0.5)
axes.plot(x, local_train, label="α=1.0 (i.e. Local Training)", linestyle='--', alpha=0.5)


axes.set_xlabel("Training Rounds", **csXYLabelFont)
axes.set_ylabel("Mean of Local Test Accuracy (%)", **csXYLabelFont)

plt.xticks(family='Times New Roman', fontsize=15)
plt.yticks(family='Times New Roman', fontsize=15)
plt.ylim(90, 100)
plt.legend(prop=legendFont)
plt.grid()
plt.show()

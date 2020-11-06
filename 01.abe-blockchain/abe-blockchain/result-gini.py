# -*- coding:utf-8 -*-
# !/usr/bin/python


import math
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.font_manager as font_manager


# calculate Gini coefficient
def Gini(wealth_list):
    # accumulate from 0
    cum_wealths = np.cumsum(sorted(np.append(wealth_list, 0)))
    sum_wealths = cum_wealths[-1]
    xarray = np.array(range(0, len(cum_wealths))) / np.float(len(cum_wealths) - 1)
    yarray = cum_wealths / sum_wealths
    # calculate the area under the curve
    B = np.trapz(yarray, x=xarray)
    # Total area of the triangle is 0.5
    A = 0.5 - B
    G = A / (A + B)
    return G


def calculate_xy_array(wealth_list):
    cum_wealths = np.cumsum(sorted(np.append(wealth_list, 0)))
    sum_wealths = cum_wealths[-1]
    xarray = np.array(range(0, len(cum_wealths))) / np.float(len(cum_wealths) - 1)
    yarray = cum_wealths / sum_wealths
    return xarray, yarray


# calculate Gini coefficient
def Gini_with_plot(wealth_list):
    xarray, yarray = calculate_xy_array(wealth_list)

    # drow the plot
    fig, axes = plt.subplots()
    axes.plot(xarray, xarray, label="Line of ideal decentralization")
    axes.plot(xarray, yarray, label="η=6, σ=5")
    axes.set_xlabel('Cumulative Percentage of organizations')
    axes.set_ylabel('Cumulative Percentage of χ')
    fig.legend()
    fig.show()


# B. Decentralization
def decentralization(eta, varphi, alpha, Upsilon, Theta, sigma):
    xi = []
    for i in range(eta):
        xi.append(1 / (2 * math.pi) ** (1 / 2) * math.e ** (-((i - eta / 2) ** 2) / (2 * sigma ** 2)))

    chi = []
    for i in range(eta):
        chi.append(Theta[i] * Upsilon[i] / (varphi ** (alpha / eta)) * xi[i])
        # chi.append(Theta[i] * Upsilon[i] * xi[i])
    return chi


def main():
    # parameters here
    sigma = 2
    eta = 4
    varphi = 2
    alpha = 6
    Upsilon = [200 for _ in range(eta)]
    Theta = [int(i % 4 > 0) for i in range(eta)]
    chi_4_2 = decentralization(eta, varphi, alpha, Upsilon, Theta, sigma)

    eta = 8
    varphi = 2
    alpha = 6
    Upsilon = [200 for _ in range(eta)]
    Theta = [int(i % 4 > 0) for i in range(eta)]
    chi_8_2 = decentralization(eta, varphi, alpha, Upsilon, Theta, sigma)

    eta = 12
    varphi = 2
    alpha = 6
    Upsilon = [200 for _ in range(eta)]
    Theta = [int(i % 4 > 0) for i in range(eta)]
    chi_12_2 = decentralization(eta, varphi, alpha, Upsilon, Theta, sigma)

    eta = 16
    varphi = 2
    alpha = 6
    Upsilon = [200 for _ in range(eta)]
    Theta = [int(i % 4 > 0) for i in range(eta)]
    chi_16_2 = decentralization(eta, varphi, alpha, Upsilon, Theta, sigma)

    xarray_6_2, yarray_6_2 = calculate_xy_array(chi_4_2)
    xarray_8_2, yarray_8_2 = calculate_xy_array(chi_8_2)
    xarray_10_2, yarray_10_2 = calculate_xy_array(chi_12_2)
    xarray_12_2, yarray_12_2 = calculate_xy_array(chi_16_2)

    # drow the plot
    fig, axes = plt.subplots()

    csfont = {'fontname': 'Times New Roman'}
    legendFont = font_manager.FontProperties(family='Times New Roman')
    xylabelFont = font_manager.FontProperties(family='Times New Roman')
    csXYLabelFont = {'fontproperties': xylabelFont}
    axesFont = font_manager.FontProperties(family='Times New Roman')
    csAxesFont = {'fontproperties': axesFont}

    axes.plot(xarray_6_2, xarray_6_2, linestyle='--', label="Line of ideal decentralization")
    axes.plot(xarray_6_2, yarray_6_2, marker="o", label="η=4, σ=2")
    axes.plot(xarray_8_2, yarray_8_2, marker="^", label="η=8, σ=2")
    axes.plot(xarray_10_2, yarray_10_2, marker="s", label="η=12, σ=2")
    axes.plot(xarray_12_2, yarray_12_2, marker="x", label="η=16, σ=2")

    axes.annotate('P(Θ) = 0.25', xy=(0.25, 0), xycoords='data',
                  xytext=(-100, 60), textcoords='offset points',
                  arrowprops=dict(arrowstyle="->", fc='0.6',
                                  connectionstyle="angle3,angleA=0,angleB=-90"),
                  family='Times New Roman')

    plt.xlabel('Cumulative proportion of organizations', fontsize=16, **csfont)
    plt.ylabel('Cumulative proportion of weights', fontsize=16, **csfont)
    plt.xticks(**csAxesFont)
    plt.yticks(**csAxesFont)
    plt.legend(prop=legendFont)
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()


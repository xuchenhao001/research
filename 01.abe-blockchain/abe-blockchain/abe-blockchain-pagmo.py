# -*- coding:utf-8 -*-
# !/usr/bin/python


import math
import numpy
import pygmo as pg
import random

# for draw plot
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as Axes3d
from pygmo.core import *


# User defined problem
def Gini(wealth_list):
    cum_wealths = numpy.cumsum(sorted(numpy.append(wealth_list, 0)))
    sum_wealths = cum_wealths[-1]
    xarray = numpy.array(range(0, len(cum_wealths))) / numpy.float(len(cum_wealths) - 1)
    yarray = cum_wealths / sum_wealths
    # calculate the area under the curve
    B = numpy.trapz(yarray, x=xarray)
    # Total area of the triangle is 0.5
    A = 0.5 - B
    G = A / (A + B)
    return G


# A. Privacy preserving
def privacy_preserving(eta, alpha, varphi, Upsilon, Theta):
    # Generate Theta list
    # variable = [1, 0]
    # weights = [P_Theta, 1 - P_Theta]
    # Theta = random.choices(variable, weights, k=eta)
    # Theta = [random.randint(0, 1) for _ in range(eta)]
    # Theta = [i % 2 for i in range(eta)]

    # Calculate the Upsilon (Privacy preserving)
    Gamma = 0
    for i in range(eta):
        Gamma_numerator = Upsilon[i] * Theta[i]
        Gamma_denominator = varphi ** (alpha / eta)
        Gamma += Gamma_numerator / Gamma_denominator
    return Gamma


# B. Decentralization
def decentralization(eta, varphi, alpha, Upsilon, Theta):
    xi = []
    sigma = 5
    for i in range(eta):
        xi.append(1 / (2 * math.pi) ** (1 / 2) * math.e ** (-((i - eta / 2) ** 2) / (2 * sigma ** 2)))

    chi = []
    for i in range(eta):
        # chi.append(Theta[i] * Upsilon[i] / (varphi ** (alpha / eta)) * xi[i])
        chi.append(Theta[i] * Upsilon[i] * xi[i])

    gini = Gini(chi)
    return gini


# C. Scalability
def scalability(lambda_enc, lambda_dec, alpha, S_tau, rho_enc, rho_dec, mu, kappa, R_trans):
    Omega_E = lambda_enc * alpha + S_tau / rho_enc
    Omega_D = lambda_dec * alpha + S_tau / rho_dec
    Omega_T = (mu + S_tau + kappa * alpha) / R_trans

    Omega = Omega_E + Omega_D + Omega_T
    return Omega


# D. Storage consumption
def storage_consumption(eta, mu, S_tau, kappa, alpha):
    Psi = eta * (mu + S_tau + kappa * alpha)
    return Psi


# For pagmo
class Schaffer:
    # Define objectives
    def fitness(self, x):
        # independent variable definition
        alpha = int(round(x[0]))
        eta = int(round(x[1]))

        # parameters here
        # print(alpha, eta, S_tau)
        # Upsilon = [random.randint(170, 210) for _ in range(eta)]
        Upsilon = [random.randint(200, 200) for _ in range(eta)]
        Theta = [i % 2 for i in range(eta)]
        lambda_enc = 0.0133
        lambda_dec = 0.0207
        rho_enc = 9574.4
        rho_dec = 13926.4
        mu = 0.016
        R_trans = 200
        kappa = 0.3333
        varphi = 2
        S_tau = 10

        pri = privacy_preserving(eta, alpha, varphi, Upsilon, Theta)
        dec = decentralization(eta, varphi, alpha, Upsilon, Theta)
        sca = scalability(lambda_enc, lambda_dec, alpha, S_tau, rho_enc, rho_dec, mu, kappa, R_trans)
        sto = storage_consumption(eta, mu, S_tau, kappa, alpha)
        return [pri, dec, sca, sto]

    # Return number of objectives
    def get_nobj(self):
        return 4

    # Return bounds of decision variables
    def get_bounds(self):
        return ([6, 7], [20, 20])

    # Return function name
    def get_name(self):
        return "Schaffer function N.1"


# 1 - Instantiate a pygmo problem constructing it from a UDP
# (user defined problem).
udp = Schaffer()
prob = pg.problem(udp)

# 2 - Instantiate a pagmo algorithm
algo = algorithm(nsga2(gen=100))
algo.set_verbosity(1)

# 3 - Instantiate populations
pop = population(prob, 40)
pop = algo.evolve(pop)


def show_fitness_fig():
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(111, projection="3d")
    # ax = fig.add_subplot(111)

    # p = numpy.array([ind.fitness.values for ind in pop.get_f()])
    p = numpy.array(pop.get_f())
    # p = numpy.array(pop.get_x())
    ax.scatter(p[:, 0], p[:, 1], p[:, 2], marker="o", s=24, label="Final Population")
    # ax.scatter(p[:, 0], p[:, 1], marker="o", s=24, label="Final Population")
    ax.view_init(elev=11, azim=-25)
    ax.autoscale(tight=True)
    plt.legend()
    plt.tight_layout()
    plt.show()


show_fitness_fig()
print("===== Here starts the fitness vectors =====")
fitness = pop.get_f()
for fit in fitness:
    fmtL = "[" + ', '.join(["{:.6f}"] * len(fit)) + "]"
    print(fmtL.format(*fit))
print("===== Here starts the chromosomes of the individuals =====")
chromosomes = pop.get_x()
for chromosome in chromosomes:
    print("[", int(round(chromosome[0])), ", ", int(round(chromosome[1])), "]")
print("===== Here starts the hypervolume of the individuals =====")
hv = hypervolume(pop)
ref_point = [2000, 20, 20, 400]
print(hv.compute(ref_point))

# print(pop)
# udp.plot(pop)

# -*- coding:utf-8 -*-
# !/usr/bin/python

import math
import numpy
import random


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
def privacy_preserving(eta, P_Theta, Upsilon):
    # Generate Theta list
    variable = [1, 0]
    weights = [P_Theta, 1 - P_Theta]
    # Theta = random.choices(variable, weights, k=eta)
    Theta = [1, 0, 1, 0, 1, 0]

    # Calculate the Upsilon (Privacy preserving)
    Gamma_numerator = 0
    Gamma_denominator = 0
    for i in range(eta):
        Gamma_numerator += Upsilon[i] * Theta[i]
        Gamma_denominator += Upsilon[i]
    Gamma = Gamma_numerator / Gamma_denominator
    return Gamma


# B. Decentralization
def decentralization(eta, Upsilon):
    xi = []
    sigma = 5
    for i in range(eta):
        xi.append(1 / (2 * math.pi) ** (1 / 2) * math.e ** (-((i - eta / 2) ** 2) / (2 * sigma ** 2)))

    chi = []
    for i in range(eta):
        chi.append(Upsilon[i] * xi[i])

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


def main():
    alpha = 12
    eta = 6
    # transaction size (KB)
    S_tau = 10
    print("Independent variable: ", alpha, eta, S_tau)

    # Calculate P_Theta (the probability of Theta) (F12)
    P_Theta = alpha / (2 * eta)

    # Generate populations for different organizations
    Upsilon = [random.randint(170, 210) for _ in range(eta)]
    print("Randomly generated org populations: ")
    print(Upsilon)

    lambda_enc = 0.0133
    lambda_dec = 0.0207
    rho_enc = 9574.4
    rho_dec = 13926.4
    mu = 0.016
    R_trans = 200
    kappa = 0.3333

    pri = privacy_preserving(eta, P_Theta, Upsilon)
    dec = decentralization(eta, Upsilon)
    sca = scalability(lambda_enc, lambda_dec, alpha, S_tau, rho_enc, rho_dec, mu, kappa, R_trans)
    sto = storage_consumption(eta, mu, S_tau, kappa, alpha)
    print("Privacy preserving: ", pri)
    print("Decentralization: ", dec)
    print("Scalability: ", sca)
    print("Storage consumption: ", sto)


if __name__ == "__main__":
    main()

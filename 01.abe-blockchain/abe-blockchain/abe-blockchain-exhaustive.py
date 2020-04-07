# -*- coding:utf-8 -*-
# !/usr/bin/python


import math
import numpy


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
def decentralization(eta, varphi, alpha, Upsilon, Theta, sigma):
    xi = []
    for i in range(eta):
        xi.append(1 / (2 * math.pi) ** (1 / 2) * math.e ** (-((i - eta / 2) ** 2) / (2 * sigma ** 2)))

    chi = []
    for i in range(eta):
        chi.append(Theta[i] * Upsilon[i] / (varphi ** (alpha / eta)) * xi[i])
        # chi.append(Theta[i] * Upsilon[i] * xi[i])

    gini = Gini(chi)
    return gini


def decentralization_pel(eta, varphi, alpha, Upsilon, Theta, sigma):
    xi = []
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


def storage_withoutabe(eta, S_tau):
    return eta * S_tau


# Adopt exhaustive method
def main():
    # independent variable definition
    # alpha = int(round(x[0]))
    # eta = int(round(x[1]))

    # parameters here
    sigma = 5
    lambda_enc = 0.0133
    lambda_dec = 0.0207
    kappa = 0.3333
    rho_enc = 9574.4
    rho_dec = 13926.4
    mu = 0.016
    R_trans = 200
    varphi = 2

    # alpha = 6
    eta = 10
    S_tau = 10
    Upsilon = [200 for _ in range(eta)]
    Theta = [i % 2 for i in range(eta)]
    for alpha in range(6, 21):
        pri = privacy_preserving(eta, alpha, varphi, Upsilon, Theta)
        dec = decentralization(eta, varphi, alpha, Upsilon, Theta, sigma)
        sca = scalability(lambda_enc, lambda_dec, alpha, S_tau, rho_enc, rho_dec, mu, kappa, R_trans)
        sto = storage_consumption(eta, mu, S_tau, kappa, alpha)
        print("chromosomes: [%3d, %3d, %3d]" % (alpha, eta, sigma),
              "fitness: [%12.6f, %12.6f, %12.6f, %12.6f]" % (pri, dec, sca, sto))


# Here starts privacy preserving
def privacy_preserving_ps():
    # parameters here
    varphi = 2
    # alpha = 6
    for eta in range(6, 21):
        alpha = eta
        Upsilon = [200 for _ in range(eta)]
        Theta = [i % 2 for i in range(eta)]
        pri = privacy_preserving(eta, alpha, varphi, Upsilon, Theta)
        print("alpha: [%3d], eta: [%3d], privacy: [%12.6f]" % (alpha, eta, pri))


def privacy_preserving_fixa():
    # parameters here
    varphi = 2
    alpha = 6
    for eta in range(6, 21):
        Upsilon = [200 for _ in range(eta)]
        Theta = [i % 2 for i in range(eta)]
        pri = privacy_preserving(eta, alpha, varphi, Upsilon, Theta)
        print("alpha: [%3d], eta: [%3d], privacy: [%12.6f]" % (alpha, eta, pri))


def privacy_preserving_csl():
    alpha = 6
    for eta in range(6, 21):
        Upsilon = [200 for _ in range(eta)]
        print("alpha: [%3d], eta: [%3d], privacy: [%12.6f]" % (alpha, eta, sum(Upsilon)))


def privacy_preserving_pelsn(sn):
    alpha = 6
    for eta in range(6, 21):
        # print("alpha: [%3d], eta: [%3d], privacy: [%12.6f]" % (alpha, eta, sn * 200/(2**(alpha/eta) - 1)))
        # print("alpha: [%3d], eta: [%3d], privacy: [%12.6f]" % (alpha, eta, sn * 200/(2**(alpha/eta))))
        print("alpha: [%3d], eta: [%3d], privacy: [%12.6f]" % (alpha, eta, sn * 200))


# Here starts decentralization
def decentralization_ps():
    # parameters here
    sigma = 5
    varphi = 2
    for eta in range(6, 21):
        Upsilon = [200 for _ in range(eta)]
        Theta = [i % 2 for i in range(eta)]
        alpha = eta
        dec = decentralization(eta, varphi, alpha, Upsilon, Theta, sigma)
        print("alpha: [%3d], eta: [%3d], decentralization: [%12.6f]" % (alpha, eta, dec))


def decentralization_fixa():
    # parameters here
    sigma = 5
    varphi = 2
    alpha = 6
    for eta in range(6, 21):
        Upsilon = [200 for _ in range(eta)]
        Theta = [i % 2 for i in range(eta)]
        dec = decentralization(eta, varphi, alpha, Upsilon, Theta, sigma)
        print("alpha: [%3d], eta: [%3d], decentralization: [%12.6f]" % (alpha, eta, dec))


def decentralization_csl():
    # parameters here
    sigma = 5
    for eta in range(6, 21):
        xi = []
        for i in range(eta):
            xi.append(1 / (2 * math.pi) ** (1 / 2) * math.e ** (-((i - eta / 2) ** 2) / (2 * sigma ** 2)))
        gini = Gini(xi)
        print("sigma: [%3d], eta: [%3d], decentralization: [%12.6f]" % (sigma, eta, gini))


def decentralization_pels1():
    # parameters here
    sigma = 5
    varphi = 2
    alpha = 6
    for eta in range(6, 21):
        Upsilon = [200 for _ in range(eta)]
        Theta = [int(eta / 2 > i >= eta / 2 - 1) for i in range(eta)]
        dec = decentralization_pel(eta, varphi, alpha, Upsilon, Theta, sigma)
        print("alpha: [%3d], eta: [%3d], decentralization: [%12.6f]" % (alpha, eta, dec))


def decentralization_pels2():
    # parameters here
    sigma = 5
    varphi = 2
    alpha = 6
    for eta in range(6, 21):
        Upsilon = [200 for _ in range(eta)]
        Theta = [int(eta / 2 + 1 > i >= eta / 2 - 1) for i in range(eta)]
        dec = decentralization_pel(eta, varphi, alpha, Upsilon, Theta, sigma)
        print("alpha: [%3d], eta: [%3d], decentralization: [%12.6f]" % (alpha, eta, dec))


def decentralization_pels3():
    # parameters here
    sigma = 5
    varphi = 2
    alpha = 6
    for eta in range(6, 21):
        Upsilon = [200 for _ in range(eta)]
        Theta = [int(eta / 2 + 2 > i >= eta / 2 - 1) for i in range(eta)]
        dec = decentralization_pel(eta, varphi, alpha, Upsilon, Theta, sigma)
        print("alpha: [%3d], eta: [%3d], decentralization: [%12.6f]" % (alpha, eta, dec))


def decentralization_pels4():
    # parameters here
    sigma = 5
    varphi = 2
    alpha = 6
    for eta in range(6, 21):
        Upsilon = [200 for _ in range(eta)]
        Theta = [int(eta / 2 + 2 > i >= eta / 2 - 2) for i in range(eta)]
        dec = decentralization_pel(eta, varphi, alpha, Upsilon, Theta, sigma)
        print("alpha: [%3d], eta: [%3d], decentralization: [%12.6f]" % (alpha, eta, dec))


def decentralization_pels5():
    # parameters here
    sigma = 5
    varphi = 2
    alpha = 6
    for eta in range(6, 21):
        Upsilon = [200 for _ in range(eta)]
        Theta = [int(eta / 2 + 3 > i >= eta / 2 - 2) for i in range(eta)]
        dec = decentralization_pel(eta, varphi, alpha, Upsilon, Theta, sigma)
        print("alpha: [%3d], eta: [%3d], decentralization: [%12.6f]" % (alpha, eta, dec))


if __name__ == "__main__":
    # Here starts privacy preserving:
    # privacy_preserving_ps()
    # privacy_preserving_fixa()
    # privacy_preserving_csl()
    # privacy_preserving_pelsn(3)
    # privacy_preserving_pelsn(4)
    # privacy_preserving_pelsn(5)

    # Here starts decentralization:
    # decentralization_ps()
    # decentralization_fixa()
    # decentralization_csl()
    # decentralization_pels1()
    # decentralization_pels2()
    # decentralization_pels3()
    # decentralization_pels4()
    decentralization_pels5()


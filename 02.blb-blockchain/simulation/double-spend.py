# -*- coding: UTF-8 -*-
import datetime
import math
import random
from numpy import random as nprandom
import string
from hashlib import sha256


##############################
# Proof of Work
##############################


def pow(eta, alpha, z):
    q = float(alpha) / eta
    d = calculate_D(q, z)
    print("POW STD \t[eta] ", eta, "\t[alpha] ", alpha, "\t[z] ", z, "\t[D] ", d)


##############################
# Proof of Stake
##############################

def pos_stake_max(eta, alpha, z, participants_stake_list):
    q = calculate_q(alpha, True, participants_stake_list)
    d = calculate_D(q, z)
    print("POS MAX \t[eta] ", eta, "\t[alpha] ", alpha, "\t[z] ", z, "\t[D] ", d)


def pos_stake_min(eta, alpha, z, participants_stake_list):
    q = calculate_q(alpha, False, participants_stake_list)
    d = calculate_D(q, z)
    print("POS MIN \t[eta] ", eta, "\t[alpha] ", alpha, "\t[z] ", z, "\t[D] ", d)


def calculate_q(alpha, isMax, participants_stake_list):
    # set those who takes minus stakes to 0
    participants_stake_list_arranged = [item if item >= 0 else -item for item in participants_stake_list]
    if isMax:
        participants_stake_list_arranged.sort(reverse=True)  # sort based on stakes, the first one is the largest one
    else:
        participants_stake_list_arranged.sort()
    attack_stake_sum = 0.0
    for index in range(alpha):
        attack_stake_sum += participants_stake_list_arranged[index]
    q = attack_stake_sum / sum(participants_stake_list_arranged)
    # print("q: ", q)
    return q


##############################
# Committee Members Auction
##############################


def cma(eta, alpha, mu, z):
    if alpha >= mu:
        q = float(choose(eta-mu, alpha-mu)) / choose(eta, alpha)
    else:
        q = 0
    d = calculate_D(q, z)
    print("CMA STD \t[eta] ", eta, "\t[alpha] ", alpha, "\t[mu] ", mu, "\t[z] ", z, "\t[D] ", d)


def calculate_D(q, z):
    p = 1 - q
    if p == 0:
        return 1.0
    lmd = z*q/p
    sum = 0
    for k in range(z+1):
        sum += (math.pow(lmd, k) * math.pow(math.e, -lmd))/math.factorial(k) * (1 - math.pow((q/p), z+1-k))
    d = 1-sum
    if d > 1.0:
        return 1.0
    else:
        return d


def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0


def calculate_mu(participants, stake_std, stake_avg, z):
    # To calculate mu
    participants_stake_list = list(nprandom.normal(loc=stake_avg, scale=stake_std, size=(participants,)))
    for mu in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
        alpha = math.floor(participants/2)
        # alpha = math.floor(participants / 4)
        mu = alpha
        # cma(participants, alpha, mu, z)
        pow(participants, alpha, z)
        # pos_stake_max(participants, alpha, z, participants_stake_list)
        # pos_stake_min(participants, alpha, z, participants_stake_list)


def calculate_eta(stake_std, stake_avg, z):
    # To calculate eta
    # for participants in [4, 6, 8, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]:
    # for participants in [4, 8, 12, 20, 32, 40, 52, 60, 72, 80, 92, 100, 112, 120, 132, 140, 152, 160, 172, 180, 192, 200]:
    for participants in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]:
        # alpha = math.floor(participants/2)
        alpha = math.floor(participants / 10)
        mu = alpha
        participants_stake_list = list(nprandom.normal(loc=stake_avg, scale=stake_std, size=(participants,)))
        # cma(participants, alpha, mu, z)
        pow(participants, alpha, z)
        # pos_stake_max(participants, alpha, z, participants_stake_list)
        # pos_stake_min(participants, alpha, z, participants_stake_list)


def calculate_alpha(participants, mu, stake_std, stake_avg, z):
    # To calculate alpha
    participants_stake_list = list(nprandom.normal(loc=stake_avg, scale=stake_std, size=(participants,)))
    for alpha in [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100]:
        # participants_stake_list = list(nprandom.normal(loc=stake_avg, scale=stake_std, size=(participants,)))
        # cma(participants, alpha, mu, z)
        pow(participants, alpha, z)
        # pos_stake_max(participants, alpha, z, participants_stake_list)
        # pos_stake_min(participants, alpha, z, participants_stake_list)


def main():
    ##############################
    # Global Parameters Set Start
    ##############################
    participants = 200
    # number of committee nodes
    mu = 100
    # number of nodes occupied by the attacker
    alpha = 100

    # standard deviation of stakes for pos
    stake_std = 15
    stake_avg = 0

    ##############################
    # Global Parameters Set End
    ##############################

    # start experiment with iterated parameters
    z = 3

    # To calculate alpha
    # calculate_alpha(participants, mu, alpha, stake_std, stake_avg)

    # To calculate eta
    calculate_eta(stake_std, stake_avg, z)

    # To calculate mu
    # calculate_mu(participants, stake_std, stake_avg, z)

if __name__ == "__main__":
    main()

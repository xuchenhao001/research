# -*- coding:utf-8 -*-
# !/usr/bin/python

import math


# n: transaction number below n
# avg: average transaction number in unit time
def sum_poisson_probability(n, avg):
    return sum((avg**k)*math.exp(-avg)/math.factorial(k) for k in range(1, n + 1))


print("In unit time on average k under n transaction number probability: ", sum_poisson_probability(60, 50))
# print("Test result: ", sum_poisson_probability(6, 3))

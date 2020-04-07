# -*- coding:utf-8 -*-
# !/usr/bin/python

# link: https://esa.github.io/pagmo2/quickstart.html

import pygmo as pg
from pygmo import *
import numpy
from math import *

# for draw plot
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as Axes3d
from pygmo.core import *


class Schaffer:
    # Define objectives
    def fitness(self, x):
        f1 = x[0]**2
        f2 = (x[0]-2)**2
        f3 = sin(x[0])
        return [f1, f2, f3]

    # Return number of objectives
    def get_nobj(self):
        return 3

    # Return bounds of decision variables
    def get_bounds(self):
        return ([-1], [2])

    # Return function name
    def get_name(self):
        return "Schaffer function N.1"


# 1 - Instantiate a pygmo problem constructing it from a UDP
# (user defined problem).
udp = Schaffer()
prob = pg.problem(udp)

# 2 - Instantiate a pagmo algorithm
algo = algorithm(nsga2(gen=200))
algo.set_verbosity(1)

# 3 - Instantiate populations
pop = population(prob, 100)
pop = algo.evolve(pop)


def show_fitness_fig():
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(111, projection="3d")
    # ax = fig.add_subplot(111)

    # p = numpy.array([ind.fitness.values for ind in pop.get_f()])
    p = numpy.array(pop.get_f())
    ax.scatter(p[:, 0], p[:, 1], p[:, 2], marker="o", s=24, label="Final Population")
    # ax.scatter(p[:, 0], p[:, 1], marker="o", s=24, label="Final Population")
    ax.view_init(elev=11, azim=-25)
    ax.autoscale(tight=True)
    plt.legend()
    plt.tight_layout()
    plt.show()


print("=====test below=====")
show_fitness_fig()

# print(pop)
# udp.plot(pop)

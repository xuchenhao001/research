# -*- coding:utf-8 -*-
# !/usr/bin/python

# link: https://esa.github.io/pagmo2/quickstart.html

import pygmo as pg
from pygmo.core import *
import numpy

# for draw plot
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as Axes3d

# 1 - Instantiate a pygmo problem constructing it from a UDP
# (user defined problem).
udp = pg.dtlz(prob_id=2, fdim=3, dim=5)
prob = pg.problem(udp)

# 2 - Instantiate a pagmo algorithm
algo = algorithm(nsga2(gen=200))
algo.set_verbosity(100)

# 3 - Instantiate populations
pop = population(prob, 100)
pop = algo.evolve(pop)


def show_fitness_fig():
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(111, projection="3d")

    # p = numpy.array([ind.fitness.values for ind in pop.get_f()])
    p = numpy.array(pop.get_f())
    ax.scatter(p[:, 0], p[:, 1], p[:, 2], marker="o", s=24, label="Final Population")
    ax.view_init(elev=11, azim=-25)
    ax.autoscale(tight=True)
    plt.legend()
    plt.tight_layout()
    plt.show()


print("=====test below=====")
show_fitness_fig()

# print(pop)
# udp.plot(pop)



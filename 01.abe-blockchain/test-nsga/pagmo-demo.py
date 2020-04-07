# -*- coding:utf-8 -*-
# !/usr/bin/python

# link: https://esa.github.io/pagmo2/quickstart.html

import pygmo as pg
from pygmo import *
import numpy

# for draw plot
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as Axes3d

# # The problem
# prob = pg.problem(pg.dtlz())
# # The initial population
# pop = pg.population(prob, size=20)
# # The algorithm (a self-adaptive form of Differential Evolution (sade - jDE variant)
# algo = pg.algorithm(pg.sade(gen=1000))
# algo.set_verbosity(100)
# # The actual optimization process
# pop = algo.evolve(pop)
# # Getting the best individual in the population
# # best_fitness = pop.get_f()[pop.best_idx()]
# # print(best_fitness)
#
# uda = algo.extract(pg.sade)
# log = uda.get_log()
# import matplotlib.pyplot as plt
#
# plt.semilogy([entry[0] for entry in log], [entry[2] for entry in log], 'k--')
# plt.show()

# ======
# udp = pg.dtlz(prob_id=2, fdim=3, dim=5)
# pop = pg.population(udp, 100)
# udp.plot(pop)
# ======

# 1 - Instantiate a pygmo problem constructing it from a UDP
# (user defined problem).
udp = pg.dtlz(prob_id=2, fdim=3, dim=5)
prob = pg.problem(udp)

# 2 - Instantiate a pagmo algorithm
algo = algorithm(moead(gen=500))
algo.set_verbosity(100)

# 3 - Instantiate populations
pop = population(prob, 45)
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



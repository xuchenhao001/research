import time, array, random, copy, math
from itertools import chain
from operator import attrgetter, itemgetter
import matplotlib as mpl
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as a3
from matplotlib.path import Path
import matplotlib.patches as patches

import numpy as np

from deap import algorithms, base, benchmarks, tools, creator
from nsgaiii import *


# In order to understand the NSGA-III selection mechanism we will make an example iteration of solving a
# three-objectives DTLZ2 problem.
creator.create("FitnessMin3", base.Fitness, weights=(-1.0,) * 3)
creator.create("Individual3", array.array, typecode='d',
               fitness=creator.FitnessMin3)


# The toolbox contains the configuration of the algorithm:
#
# how to create an individual,
# how to create a population,
# the evolutionary operators,
# the evaluation function, and
# the selection method.
# The prepare_toolbox() function encapsulates the configuration.
def prepare_toolbox(problem_instance, selection_func, number_of_variables, bounds_low, bounds_up):
    def uniform(low, up, size=None):
        try:
            return [random.uniform(a, b) for a, b in zip(low, up)]
        except TypeError:
            return [random.uniform(a, b) for a, b in zip([low] * size, [up] * size)]

    toolbox = base.Toolbox()

    toolbox.register('evaluate', problem_instance)
    toolbox.register('select', selection_func)

    toolbox.register("attr_float", uniform, bounds_low, bounds_up, number_of_variables)
    toolbox.register("individual", tools.initIterate, creator.Individual3, toolbox.attr_float)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("mate", tools.cxSimulatedBinaryBounded,
                     low=bounds_low, up=bounds_up, eta=20.0)
    toolbox.register("mutate", tools.mutPolynomialBounded,
                     low=bounds_low, up=bounds_up, eta=20.0,
                     indpb=1.0 / number_of_variables)

    toolbox.pop_size = 100  # population size
    toolbox.max_gen = 200  # max number of iteration
    toolbox.mut_prob = 1 / number_of_variables
    toolbox.cross_prob = 0.3

    return toolbox


def problem(individual):
    return benchmarks.dtlz2(individual, 3)


# Preparing an instance of toolbox
number_of_variables = 30
bounds_low, bounds_up = 0, 1
toolbox = prepare_toolbox(problem,
                          sel_nsga_iii, number_of_variables,
                          bounds_low, bounds_up)


def nsga_iii(toolbox, stats=None, verbose=False):
    population = toolbox.population(n=toolbox.pop_size)
    return algorithms.eaMuPlusLambda(population, toolbox,
                              mu=toolbox.pop_size,
                              lambda_=toolbox.pop_size,
                              cxpb=toolbox.cross_prob,
                              mutpb=toolbox.mut_prob,
                              ngen=toolbox.max_gen,
                              stats=stats, verbose=verbose)


stats = tools.Statistics()
stats.register('pop', copy.deepcopy)
res, logbook = nsga_iii(toolbox, stats=stats)

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection='3d')

for ind in res:
    ax.scatter(ind.fitness.values[0],
               ind.fitness.values[1],
               ind.fitness.values[2], marker='o', color='mediumpurple')

ax.set_xlabel('$f_1()$', fontsize=15)
ax.set_ylabel('$f_2()$', fontsize=15)
ax.set_zlabel('$f_3()$', fontsize=15)
ax.view_init(elev=11, azim=-21)
plt.autoscale(tight=True)
plt.show()

csfont = {'fontname': 'Times New Roman'}
# Plotting hypervolume
pops = logbook.select('pop')
from deap.tools._hypervolume import hv
def hypervolume(individuals, ref=None):
    front = tools.sortLogNondominated(individuals, len(individuals), first_front_only=True)
    wobjs = np.array([ind.fitness.wvalues for ind in front]) * -1
    if ref is None:
        ref = np.max(wobjs, axis=0) + 1
    return hv.hypervolume(wobjs, ref)
pops_obj = [np.array([ind.fitness.wvalues for ind in pop]) * -1 for pop in pops]
ref = np.max([np.max(wobjs, axis=0) for wobjs in pops_obj], axis=0) + 1
hypervols = [hypervolume(pop, ref) for pop in pops]
plt.plot(hypervols)
plt.xlabel('Iterations (t)', fontsize=16, **csfont)
plt.ylabel('Hypervolume', fontsize=16, **csfont)
plt.grid()
plt.show()

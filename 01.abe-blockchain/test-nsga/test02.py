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
from functools import reduce
from math import sin, cos, pi, exp, e, sqrt
from operator import mul


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
    # def uniform(low, up, size=None):
    #     return [random.randint(low, up) for i in range(size)]
    def uniform(low, up, size=None):
        return [random.randint(low, up) for i in range(size)]

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
    obj = 3
    xc = individual[:obj-1]
    xm = individual[obj-1:]
    g = sum((xi-0.5)**2 for xi in xm)
    f = [(1.0+g) * reduce(mul, (cos(0.5*xi*pi) for xi in xc), 1.0)]
    f.extend((1.0+g) * reduce(mul, (cos(0.5*xi*pi) for xi in xc[:m]), 1) * sin(0.5*xc[m]*pi) for m in range(obj-2, -1, -1))

    return f


def my_problem(individual):
    xm = individual
    f = [sum((xi - 0.5) ** 2 for xi in xm)]
    f.extend([sum((1/xi) ** 2 for xi in xm)])


    # x = individual
    # f = 0.036*x + 0.014
    # f.extend(1.8556*x)

    return f


# Preparing an instance of toolbox
number_of_variables = 100
bounds_low, bounds_up = 1, 30
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


def show_result(res, logbook):
    res_set = []
    for item in res:
        res_set.append((item.fitness.values[0], item.fitness.values[1]))
    print("Result set: ", res_set)

    individual_set = []
    pops = logbook.select('pop')
    for pop in pops:
        individual_set.append(pop)
    print(individual_set)


show_result(res, logbook)


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
plt.xlabel('Iterations (t)')
plt.ylabel('Hypervolume')
plt.show()

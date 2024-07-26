import numpy as np

def select(population, num_parents, fitness):
    population_size = population.shape[0]
    parents = population[np.random.choice(population_size, num_parents, p=fitness/fitness.sum())]
    return parents

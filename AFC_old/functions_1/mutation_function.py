import numpy as np

def mutate(new_population, mutation_rate, mutation_range):
    population_size = new_population.shape[0]
    num_variables = new_population.shape[1]

    mutated_population = new_population.copy()

    for i in range(population_size):
        for j in range(num_variables):
            if np.random.rand() < mutation_rate:
                mutation_value = (np.random.rand() - 0.5) * 2 * mutation_range[j]
                mutated_population[i, j] = mutated_population[i, j] + mutation_value
                mutated_population[i, j] = max(lower_bounds[j], min(upper_bounds[j], mutated_population[i, j]))

    return mutated_population
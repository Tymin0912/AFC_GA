Read Me file for Genetic Algorithm code.

STILL NEED TO DO:
- You need to write code to save the .csv files where you want them and have them indexed so that the 
fitness function can take the right files and calculate the efficiency.
- Write the code that does the hdawg stuff so that when you run the code it will run the sequence_params.
- These parts are highlighted with ### in the HOW TO USE section.


Pesudo Code: 
NOTE: This is for when the code worked with arrays it now does it all in dictionaries. same concept.
-Creates a random population of size N
-Individuals in the population are arrays [x,x,x,x,x]
-Each variable is a parameters used for one of the steps in the sequence (i.e the pit params)
-We calculate how good each individual is by the fitness function (looking at how good the echo is)
-We then randomly select (with a weighted distribution based on the fitness) a percentage of the population to become the parents.
-We crossover (with a crossover rate) the parents by randomly switching some of the variables with each other this becomes the new population
If they do not crossover they get copied directly into the new population
-This repeats until the new population fills up to its original size N
-We now mutate (with a mutation rate. Only a certain percentage will mutate) every variable within a specific mutation range
-This our new population generation 2 we repeat this process untill we reach a certain number of generations or a specific fitness.


HOW TO USE:
# The functions are all in GA_functions.ipynb 
# NOTE: Use old fitness fuction (or write your own depending on what you want to base the fitness on)

import numpy as np
import pandas as pd

# Define the GA parameters how GA will preform NOTE: DO NOT CHANGE VARIABLE NAMES
# mutation range is the percent a parameter can mutate by (percent of the upper bound)
GA_params = { 'population_size': 1,
             'num_parents': 1,
             'num_generations': 1,
             'crossover_rate': 0.8,
             'mutation_rate': 0.9,
             'mutation_range': 0.1}

# Make your sequence you want to run add bounds (x,y) for the range you want and a single value if you want it constant 
# (NOTE: amplitude max 0.21) this is sequence_params 
sequence_params_GA = dict(
    bounds_pit = {'no_pulses': (1, 1001),
                 'f_0': 250E6,
                'amplitude': (0.001, 0.21),
                'f_sweep': 12E6/4,
                'duration': (10E-6, 100E-6),
                'delay': (10E-6, 300E-6),
                'phase': 0},

    bounds_burn_back = {'no_pulses': (1, 1001),
                'f_0': (10E5, 500E6),
                'amplitude': (0.001, 0.21),
                'freq_sweep': (0.1E-6, 5E6),
                'duration': (10E-6, 100E-6),
                'delay': (10E-6, 300E-6),
                'phase': 0},

    bounds_clean = {'no_pulses': (1, 1001),
                'f_0': (10E5, 500E6),
                'amplitude': (0.001, 0.21),
                'freq_sweep': (0.1E-6, 5E6),
                'duration': (10E-6, 100E-6),
                'delay': (10E-6, 300E-6),
                'phase': 0}
)

# This generates the inital population for the GA gen 0 
sequence_params = initial_population(GA_params, sequence_params_GA)

# This is to save all the populations and their fitnesses 
params_GA_save = {key: [] for key in sequence_params}
fit = np.zeros((GA_params['num_generations']),(GA_params['population_size']))

for i in range(GA_params['num_generations']):     # Loop to go through each generation

    for j in range(GA_params['population_size']): # Loop to go though each individual
        ### compile and upload to HDAWG
        ### Run HDAWG Sequence  
        ### run code with this line below this line is what your sequence_params is  
        run_hdawg = {key: sequence_params[key][j] for key in sequence_params}

        ### save echo_data_folder{j}, input_data_folder{j}, cross_data_folder{j} 
        ### Recommend to save folders gen_{i} and then the above inside these 
        ### You will need to change the fitness folder to correctly pick the right files 
        ### (This has already been done previously so you can modify the old code. ask Finley)
        fit[i,j] = fitness(echo_data_folder, input_data_folder, cross_data_folder)

    # Saves the population
    for key in sequence_params:
        params_GA_save[key].extend(sequence_params[key])

    # 1. Selects the parents 2. crossover and breeding new population 3. mutates new population
    parent_population = parentselect(sequence_params, GA_params, fit[i,:])
    new_sequence_params = crossover(parent_population, GA_params)
    sequence_params = mutate(new_sequence_params, GA_params, sequence_params_GA)

# After GA finishes running this will give you the best solution found 
optimal_params = optimal_solution(fit, params_GA_save, GA_params)
print("\Optimal Params :\n", optimal_params)



Additional Notes:
- You may only need a small population size for GA to work instead of large one. 
Why: if the optimal solution is hard to come by then most of the pop will be 0.
So if you have a large pop and you manage to get one good solution it may be drowned out due to the amount of bad solutions.  
- The GA_params rates and range may not be optimal you will need to try out different values to get the best results
- GA_params we have seen to work well in other cases:
GA_params = { 'population_size': 10, # need to test more but 10-20 seem to work fine 
             'num_parents': 5,       # 50% of pop_size seems best
             'num_generations': 5,   # doesnt really matter more dependant on how much time you want to spend on it
             'crossover_rate': 0.8,  # 80% seems best
             'mutation_rate': 0.01,  # 1% seems best
             'mutation_range': 0.05} # need to test this out as previously it was individual values for each param


Future things to do/implement:
- Make new parentselect function that does a tournement style selection (Atm its random wheel with weighted prob.)
- Instead of having fully random initial population you can insert multiple good individuals (you may need to have several copies of them if you have large population size as they might get drowned out)
- Add a visual so you can see how each gen improves (i.e plot the best individual of each gen)
- If you want make it have individual mutation range for each param (this will become very big if you have a big sequence_params it might not be worth doing)
- Add a break out point so if you get a certain efficiency (fitness) you desire it will stop the code (it will save a lot more time. no need to run the how algorithm)
- 

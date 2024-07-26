import os
import sys

# Parent directory to import the functions package
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from functions import fitness, select, crossover, mutate    # Importing the functions 

# Defining the path to the folder containing the echo data CSV files. Used for fitness function
echo_data_folder = os.path.join(os.path.dirname(__file__), 'echo_data')


fit = fitness(echo_data_folder)
print(fit)

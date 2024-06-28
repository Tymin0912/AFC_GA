import numpy as np
import pandas as pd
import os

def fitness(echo_data_folder):

    file_columns = {
        '0_echo.csv': 2,                   # Second column of file 0_echo.csv
        '0_input_cross.csv': 2,            # Second column of file 0_input_cross.csv
        '0_input_no_rephasing.csv': 2      # Second column of file 0_input_no_rephasing.csv
    }

    # Dictionary to store DataFrames
    data_frames = {}
    
    # Read each file into the dictionary
    for filename, col_index in file_columns.items():
        file_path = os.path.join(echo_data_folder, filename)
        data_frames[filename] = pd.read_csv(file_path)
    
    # Assign variables to the second C_2 (V)
    echo_col, cross_col, no_rephasing_col = [
    data_frames[filename].iloc[:, col_index]
    for filename, col_index in file_columns.items()
    ]

    # For smoothing data
    kernal_size = 10
    kernal = np.transpose(np.ones(kernal_size)/kernal_size)

    cross = np.convolve(cross_col,kernal,mode='same')
    no_rephasing = np.convolve(no_rephasing_col,kernal,mode='same')
    echo = np.convolve(echo_col,kernal,mode='same')

    # Finding the area
    x = np.arange(len(echo))
    area_echo = np.trapezoid(echo,x)
    area_cross = np.trapezoid(cross,x)
    area_no_rephasing = np.trapezoid(no_rephasing,x)

    # Finding the efficiency
    fitness = (area_echo-area_no_rephasing)/area_cross

    return fitness
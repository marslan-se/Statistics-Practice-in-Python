# Import relevant Python libraries.
import numpy as np
import pandas as pd

# RUN THIS CELL TO IMPORT YOUR DATA.
file_name = "c4_epa_air_quality.csv"
epa_data = pd.read_csv(file_name, index_col=0)

# Display first 10 rows of the data.
print(epa_data.head(10))

# Get descriptive stats.
print(epa_data['aqi'].describe())

# Get descriptive stats about the states in the data.
print(epa_data['state_name'].describe())

# Compute the mean value from the aqi column.
print(np.mean(epa_data['aqi']))

# Compute the median value from the aqi column.
print(np.median(epa_data['aqi']))

# Identify the minimum value from the aqi column.
print(np.min(epa_data['aqi']))

# Identify the maximum value from the aqi column.
print(np.max(epa_data['aqi']))

# Compute the standard deviation for the aqi column.
print(np.std(epa_data['aqi']))
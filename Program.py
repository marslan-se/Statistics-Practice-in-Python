# Import relevant Python libraries.
import numpy as np
import pandas as pd

# RUN THIS CELL TO IMPORT YOUR DATA.
file_name = "c4_epa_air_quality.csv"
epa_data = pd.read_csv(file_name, index_col=0)

# Display first 10 rows of the data.
print("First 10 rows of the data:")
print(epa_data.head(10))

# Get descriptive stats for the 'aqi' column.
print("\nDescriptive statistics for AQI:")
print(epa_data['aqi'].describe())

# Get descriptive stats about the states in the data.
print("\nDescriptive statistics for states:")
print(epa_data['state_name'].describe())

# Compute and print the mean value from the 'aqi' column.
print("\nMean AQI:", np.mean(epa_data['aqi']))

# Compute and print the median value from the 'aqi' column.
print("Median AQI:", np.median(epa_data['aqi']))

# Identify and print the minimum value from the 'aqi' column.
print("Minimum AQI:", np.min(epa_data['aqi']))

# Identify and print the maximum value from the 'aqi' column.
print("Maximum AQI:", np.max(epa_data['aqi']))

# Compute and print the standard deviation for the 'aqi' column.
print("Standard Deviation of AQI:", np.std(epa_data['aqi']))
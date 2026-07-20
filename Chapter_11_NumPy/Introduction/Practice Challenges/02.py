'''
Outlier Filtering: Ek temperature sensor ka data array banayein. Usme se wo saari abnormal values remove karein jo mean se 3 standard deviations door (3 * np.std()) hain.
'''
import numpy as np

arr_t2 = np.array([15, 16, 14, 15, 100, 15, 14, -50, 16])
print(f"Original Data: {arr_t2}")

mean = np.mean(arr_t2)
std_dev = np.std(arr_t2)

lower_bound = mean - (3 * std_dev)
higher_bound = mean + (3 * std_dev)

cleaned_data = arr_t2[(arr_t2 >= lower_bound) & (arr_t2 <= higher_bound) ]
print(f"Mean: {mean:.2f}")
print(f"Std Dev: {std_dev:.2f}")
print(f"Valid Range: From: {lower_bound:.2f} To:  {higher_bound:.2f}")
print(f"Cleaned Data: {cleaned_data}")
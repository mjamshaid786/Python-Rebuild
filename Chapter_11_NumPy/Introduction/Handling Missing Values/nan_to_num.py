import numpy as np

# np.nan_to_num(array, nan=value) Default = 0

arr = np.array([1, 2, 5, 7, np.nan, 8])
print(np.isnan(arr))
new_arr = np.nan_to_num(arr, nan=0)
print(new_arr)
print(np.isnan(new_arr))

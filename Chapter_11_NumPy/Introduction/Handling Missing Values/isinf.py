import numpy as np

# np.isinf(array) is used to detect infinity values

arr = np.array([1, 2, 5, 7, np.inf, 8])
print(np.isinf(arr))

# replacing inf values

new_arr = np.nan_to_num(arr, posinf=100, neginf=-100) # positive inf, negative if

print(new_arr)
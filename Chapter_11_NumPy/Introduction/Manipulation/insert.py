
import numpy as np
arr = np.array([1, 2, 5, 7, 6, 8])
print(arr)

new_arr = np.insert(arr, 2, 3,)
print(new_arr)

# 2D array insert

arr_2d = np.array([[1, 2],
                   [3, 4]])
print(arr_2d)

new_2d_arr = np.insert(arr_2d, 2, [5, 6], axis=1)
print(new_2d_arr)
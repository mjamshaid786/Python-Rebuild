import numpy as np


# isnan(array) will detect null values and return true or false

arr = np.array([1, 2, np.nan, 8, 6, 8])
print(np.isnan(arr))
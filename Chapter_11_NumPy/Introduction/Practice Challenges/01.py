'''
Missing Values Handling: Ek dataset array me kuch np.nan (missing values) hain. Un saari missing values ko identify karo aur unhe poore array ke mean (average) se replace karo.
'''

import numpy as np
arr_t1 = np.array([10.0, 20.0, np.nan, 40.0, np.nan, 60.0])

identify = np.isnan(arr_t1)
print(identify)

cleaned_data = np.nan_to_num(arr_t1, nan=np.nanmean(arr_t1)) # here np.nanmean method is used to replace nan values with the mean of array
print(cleaned_data)
'''
9.	Filtering with Boolean Masking: Ek employee salary array me se sirf un salaries ko extract karo jo 50,000 se zyada aur 100,000 se kam hon
'''
import numpy as np
arr_t9 = np.array([45000, 60000, 120000, 75000, 40000, 90000])

limit = arr_t9[(arr_t9 > 50000) & (arr_t9 < 100000)]
print(limit)
'''
3.	Invalid Data Remediation: Ek financial transaction array me se saari negative values aur np.inf (infinity) values ko filter out karke zero set karo.
'''

import numpy as np
arr_t3 = np.array([500.0, -200.0, 300.0, np.inf, 1000.0, -50.0])
print(f"Original Data: {arr_t3}")

check = np.isinf(arr_t3)
print(check)

invalid_mask = (arr_t3 < 0) | np.isinf(arr_t3)
arr_t3[invalid_mask] = 0
print(f"Cleaned Data: {arr_t3}")
'''
10.	Finding Top N Records: Ek website traffic hits ka array hai. np.argsort() ka use karke un top 5 hours ke indices (positions) pata karo jahan sabse zyada traffic tha.
'''

import numpy as np
arr_t10 = np.array([150, 500, 200, 1000, 50, 800, 400])
sort = np.argsort(arr_t10)
print(sort)
top_3 = sort[-3:]
print(top_3)
top_3_vales = arr_t10[top_3]
print(top_3_vales)
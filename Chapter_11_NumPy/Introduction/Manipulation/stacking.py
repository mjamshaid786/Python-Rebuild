import numpy as np

arr = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# vstack() it will add rows

vstk = np.vstack((arr, arr2))
print(vstk)

#hstack((arr1, arr2)) will add array to column

hstk = np.hstack((arr, arr2))
print(hstk)
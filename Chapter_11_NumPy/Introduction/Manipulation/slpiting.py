import numpy as np

arr = np.array([1, 2, 5, 7, 6, 8])
print(np.split(arr, 2)) # split into equal parts

# vsplit(arraqy, parts)
arr1 = np.array([[2, 4, 5],
                 [4, 6, 1]])
print(np.vsplit(arr1, 2))
# hsplit
print(np.hsplit(arr1, 1))
 
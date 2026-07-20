import numpy as np

# shape will tell you how many rows and columns your array has (2, 3)


arr_2d = np.array([1, 2, 3])

print(arr_2d.shape)# it will print (2, 3) 2 rows and 3 columns

# size will tell how many elemets are in your array
print(arr_2d.size) # will print 6

# ndim is used to check the dimension of array
print(arr_2d.ndim)

#dtype check data type of elements
print(arr_2d.dtype)

# astype for typecasting
#arr.astype(required data type)
flt = arr_2d.astype(float)
print(flt)
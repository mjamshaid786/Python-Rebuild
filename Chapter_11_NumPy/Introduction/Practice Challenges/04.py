'''
4.	Data Type Casting: Ek array me numbers string format me hain ["10.5", "20.1", "30.8"]. Isay bina kisi data loss ke proper float64 format me convert karo.
'''
import numpy as np
arr_t4 = np.array(["10.5", "20.1", "30.8"])

flt = arr_t4.astype(float)
print(flt)
print(flt.dtype)
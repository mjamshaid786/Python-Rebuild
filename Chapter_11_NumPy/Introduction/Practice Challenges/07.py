'''
7.	Data Clipping for Safety: Ek user ratings array (scale 0-100) me kuch system errors ki wajah se -5 aur 115 jaisi values aa gayi hain. Unhe clip karo taaki min value 0 aur max value 100 ho jaye.
'''
import numpy as np
arr_t7 = np.array([-5, 20, 50, 95, 115, 80])
print(f"Original Data: {arr_t7}")
# np.clip(array, min_bound, max_bound)
cleaned_data = np.clip(arr_t7, 0, 100)
print(f"Updated Data: {cleaned_data}")

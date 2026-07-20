'''
6.	Removing Duplicates: Ek network logs incoming IP IDs ka array hai. Unme se saari duplicate entries ko remove karke sirf unique IDs ki list nikaalo.
'''
import numpy as np
arr_t6 = np.array([101, 102, 101, 103, 104, 102, 105])

cleaned_data = np.unique(arr_t6)
print(cleaned_data)


#Trick found
# np.uniques also return no.of occurances
unique_elements, counts = np.unique(arr_t6, return_counts=True)
print(f"Unique IDs: {unique_elements}\nOccurances: {counts}")
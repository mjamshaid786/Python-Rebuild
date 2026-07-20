'''
5.	Conditional Flagging (Binarization): Ek age group ka array hai. Agar age 18 ya usse zyada hai toh usay 1 (Adult) aur agar kam hai toh 0 (Minor) se replace karo bina loop lagaye.
'''
import numpy as np
arr_t5 = np.array([12, 18, 25, 14, 40, 17])
#np.where(condition, if_true, if_false)
cleaned_data = np.where(arr_t5 >= 18, 1, 0) # Love this method
print(cleaned_data)
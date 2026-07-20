'''
8.	Combining Multi-Source Logs: Do alag-alag server nodes se aane waale 1D arrays ko horizontal aur vertical dono tareeqon se merge (concatenate) karo.
'''
import numpy as np

arr_t8_node1 = np.array([1, 2, 3])
arr_t8_node2 = np.array([4, 5, 6])

print(np.vstack((arr_t8_node1, arr_t8_node2)))
print(np.hstack((arr_t8_node1, arr_t8_node2)))

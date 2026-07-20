import numpy as np

board = np.array([
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 0]  
])


total = np.sum(board[:, 0])
print(total)
if total == 3:
    print("Win")
else:
    print("Loss")

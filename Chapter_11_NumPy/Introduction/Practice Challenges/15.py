import numpy as np

board = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]  # Diagonal par teeno 1 hain!
])

total = np.sum(np.diag(board))
print(total)
if total == 3:
    print("Win")
else:
    print("Loss")

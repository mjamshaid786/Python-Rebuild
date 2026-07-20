import numpy as np

board = np.array([
    [0, 0, 0],
    [0, 0, 0],  
    [0, 0, 0]
])


# board[1, 1] = 1
# print(board)
# board[0, 2] = 1
# print(board)
board[:, 0] = 1
print(board)
board[0, :] = 1
print(board)
board[:, 2] = 0
print(board)
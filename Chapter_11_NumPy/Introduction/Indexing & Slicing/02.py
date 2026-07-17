import numpy as np

prices = np.array([10, 20, 30, 40, 50])

# print(prices[0])
first_window = prices[:3]
print(first_window)
mean = np.mean(first_window)
print(mean)



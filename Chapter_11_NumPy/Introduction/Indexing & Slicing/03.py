import numpy as np

sensor_data = np.array([15, 18, 20, 22, 25, 28, 30, 29, 27, 24, 20, 17])

shaped = sensor_data.reshape(3, 4)
print(shaped)
import numpy as np
import random
arr1 = np.array(random.sample(range(1, 11), 10))
print("1D Array:")
print(arr1)
arr2 = np.array(random.sample(range(1, 10), 9)).reshape(3, 3)
print("\n2D Array:")
print(arr2)
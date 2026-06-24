import numpy as np

a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

first_row = a[0, :]
print("First Row:")
print(first_row)

second_col = a[:, 1]
print("\nSecond Column:")
print(second_col)

element_50 = a[1, 1]
print("\nElement 50:")
print(element_50)
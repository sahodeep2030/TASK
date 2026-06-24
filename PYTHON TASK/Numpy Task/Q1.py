import numpy as np

a = np.array([
    [11, 22, 33],
    [44, 55, 66],
    [77, 88, 99]
])

first_col = a[:, 0]
print("First Column:")
print(first_col)

last_row = a[-1, :]
print("\nLast Row:")
print(last_row)

sub_matrix = a[0:2, 1:3]
print("\nExtracted Sub-matrix:")
print(sub_matrix)
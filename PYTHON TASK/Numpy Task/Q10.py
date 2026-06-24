import numpy as np

a = np.array([[1,2,3],
              [4,5,6]])

print("Array:")
print(a)

print("Shape =", a.shape)
print("Size =", a.size)
print("Dimensions =", a.ndim)
print("Datatype =", a.dtype)

b = a.astype(float)

print("\nAfter datatype conversion:")
print(b)
print("Datatype =", b.dtype)
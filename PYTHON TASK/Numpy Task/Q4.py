import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 1. Addition
add_result = a + b
print("Addition:", add_result)

# 2. Subtraction
sub_result = a - b
print("Subtraction:", sub_result)

# 3. Multiplication
mul_result = a * b
print("Multiplication:", mul_result)

# 4. Division
div_result = a / b
print("Division:", div_result)

# 5. Power of 3
pow_result = a ** 3
print("Power of 3 (for array 'a'):", pow_result)
pow_result = b ** 3
print("Power of 3 (for array 'b'):", pow_result)

# 6. Square
square_result = a ** 2
print("Square (for array 'a'):", square_result)
square_result = b ** 2
print("Square (for array 'b'):", square_result)

# 7. Mean 
mean_a = np.mean(a)
mean_b = np.mean(b)
print("Mean of array 'a':", mean_a)
print("Mean of array 'b':", mean_b)
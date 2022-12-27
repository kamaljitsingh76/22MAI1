# Python program to demonstrate
# basic operations on single array
import numpy as np

a = np.array([1, 2, 5, 3])

# add 1 to every element
print("Adding 1 to every element:", a + 1)

# subtract 3 from each element
print("Subtracting 3 from each element:", a - 3)

# multiply each element by 10
print("Multiplying each element by 10:", a * 10)

# square each element
print("Squaring each element:", a ** 2)

# modify existing array
a *= 2
print("Doubled each element of original array:", a)

# transpose of array
a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]])

print("\nOriginal array:\n", a)
print("Transpose of array:\n", a.T)

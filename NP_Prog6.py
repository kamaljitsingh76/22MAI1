# Python program to demonstrate
# universal functions in numpy
import numpy as np

# create an array of sine values
a = np.array([0, np.pi / 2, np.pi])
print("Sine values of array elements:", np.sin(a))

# exponential values
a = np.array([0, 1, 2, 3])
print("Exponent of array elements:", np.exp(a))

# square root of array values
print("Square root of array elements:", np.sqrt(a))

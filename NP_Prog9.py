import numpy as np

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])
print("Array a:\n",a)
print("\nArray b:\n",b)
# vertical stacking
print("Vertical stacking:\n", np.vstack((a, b)))

# horizontal stacking
print("\nHorizontal stacking:\n", np.hstack((a, b)))

c = [5, 6]

# stacking columns
print("\nColumn stacking:\n", np.column_stack((a, c)))

# concatenation method
print("\nConcatenating to 2nd axis:\n", np.concatenate((a, b), 1))

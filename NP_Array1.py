import numpy as np
x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]])
print('Our array is:')
print(x)
print('\n')
# Now we will print the items greater than 5
print('The items greater than 5 are:')
print( x[x > 5])

import numpy as np
a = np.array([[3,7,5],[8,4,3],[2,4,9]])
print('Our array is:')
print(a)
print('\n')
print('Applying ptp() function:')
print(np.ptp(a))
print('\n')
print('Applying ptp() function along axis 1:')
print(np.ptp(a, axis = 1))
print('\n')
print('Applying ptp() function along axis 0:')
print(np.ptp(a, axis = 0))


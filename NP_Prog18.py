import numpy as np
a = np.array([0,30,45,60,90])
print('Sine of different angles:')
# Convert to radians by multiplying with pi/180
print(np.sin(a*np.pi/180))
print('\n')
print('Cosine values for angles in array:')
print(np.cos(a*np.pi/180))
print('\n')
print('Tangent values for given angles:')
print(np.tan(a*np.pi/180))

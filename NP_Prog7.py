import numpy as np
a = np.array([1,2,3,4,5,6])
print(a)
a = a.reshape(3,2)
print(a)
a = a.reshape(2,-1)
print(a)
a = a.ravel()
print(a)
a = np.arange(10).reshape(5,2)
print(a)
a = a.T 
print(a)
a = a.transpose((1,0))
print(a)

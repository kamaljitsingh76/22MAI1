'''
the indices can be completely different, as in the following example.
We have two indices. One is the Turkish translation of the English fruit names:
'''
import numpy as np
import pandas as pd

fruits = ['apples', 'apples', 'cherries', 'pears']
fruits_tr = ['elma', 'portakal', 'kiraz', 'armut']

S = pd.Series([20, 33, 52, 10], index=fruits)
S2 = pd.Series([17, 13, 31, 32], index=fruits_tr)
'''
print(S + S2)

# It's possible to access single values of a Series
print(S['apples'])


Series objects can also be accessed by multiple indexes at the same time. 
This can be done by packing the indexes into a list. 
This type of access returns a Pandas Series again:

print(S[['apples', 'oranges', 'cherries']])


Similar to Numpy we can use scalar operations or mathematical functions on a series:
'''
print(S)

#print((S + 3) * 4)

#print("======================")
#print(np.sin(S))
'''
'''
'''
Series.apply(func, convert_dtype=True, args=(), **kwds)
The function "func" will be applied to the Series and it returns either a Series or a DataFrame, depending on "func".

'''
#print("----------------------")
#print(S.apply(np.sin))


'''
We can also use Python lambda functions. 
If there are less than 50 available, we will augment the stock by 10:
'''
#print("----------------------")
#print(S.apply(lambda x: x if x > 50 else x+10 ))

'''
Similar to numpy arrays, we can filter Pandas Series with a Boolean array:
'''
#print(S[S>30])

'''
A series can be seen as an ordered Python dictionary with a fixed length.
'''
print("apples" in S)


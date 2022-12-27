'''
The indices do not have to be the same for the Series addition.
The index will be the "union" of both indices.
If an index doesn't occur in both Series, the value for this Series will be NaN:
'''

import pandas as pd

fruits = ['peaches', 'oranges', 'cherries', 'pears']
fruits2 = ['raspberries', 'oranges', 'cherries', 'pears']

S = pd.Series([20, 33, 52, 10], index=fruits)
S2 = pd.Series([17, 13, 31, 32], index=fruits2)
print(S + S2)


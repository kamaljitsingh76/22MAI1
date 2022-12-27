# Connection between NaN and None
import pandas as pd
d = {"a":23, "b":45, "c":None, "d":0}
S = pd.Series(d)
print("Null values are true:\n",S)
print("-----------------------")
print(pd.isnull(S))

print("-----------------------")
print(pd.notnull(S))


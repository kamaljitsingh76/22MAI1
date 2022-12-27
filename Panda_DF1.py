import pandas as pd

years = range(2014, 2018)

shop1 = pd.Series([2409.14, 2941.01, 3496.83, 3119.55], index=years)
shop2 = pd.Series([1203.45, 3441.62, 3007.83, 3619.53], index=years)
shop3 = pd.Series([3412.12, 3491.16, 3457.19, 1963.10], index=years)

print(pd.concat([shop1, shop2, shop3]))

# Let's do it with "axis=1":
print("----------------------------------------")

shops_df = pd.concat([shop1, shop2, shop3], axis=1)
print(shops_df)

# Let's do some fine sanding by giving names to the columns:
print("----------------------------------------")
cities = ["Zürich", "Winterthur", "Freiburg"]
shops_df.columns = cities
print(shops_df)


# alternative way: give names to series:
shop1.name = "Zürich"
shop2.name = "Winterthur"
shop3.name = "Freiburg"

print("-------------------------------")
shops_df2 = pd.concat([shop1, shop2, shop3], axis=1)
print(shops_df2)

#what kind of data type is our result
print("----------------------------------------")
print(type(shops_df))
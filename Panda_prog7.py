'''
Creating Series Objects from Dictionaries
'''
import pandas as pd
cities = {"London":    8615246,
          "Berlin":    3562166,
          "Madrid":    3165235,
          "Rome":      2874038,
          "Paris":     2273305,
          "Vienna":    1805681,
          "Bucharest": 1803425,
          "Hamburg":   1760433,
          "Budapest":  1754000,
          "Warsaw":    1740119,
          "Barcelona": 1602386,
          "Munich":    1493900,
          "Milan":     1350680}

city_series = pd.Series(cities)
print(city_series)



# NaN - Missing Data

my_cities = ["London", "Paris", "Zurich", "Berlin",
             "Stuttgart", "Hamburg"]

my_city_series = pd.Series(cities, index=my_cities)
print("---------------------------")
print(my_city_series)



my_cities = ["London", "Paris", "Berlin", "Hamburg"]

my_city_series = pd.Series(cities, index=my_cities)

print(my_city_series)


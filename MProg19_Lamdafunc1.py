# Python Lambda Function Example

str1 = 'This is String'

# lambda returns a function object
rev_upper = lambda string: string.upper()[::-1]
print(rev_upper(str1))




# Example 1: Condition Checking Using Python lambda function

format_numeric = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"

print("Int formatting:", format_numeric(1000000))
print("float formatting:", format_numeric(999999.789541235))





#Example 2: Difference Between Lambda functions and def defined function

def cube(y):
    return y * y * y

def lambda_cube(y): return y * y * y

# using function defined
# using def keyword
print("Using function defined with `def` keyword, cube:", cube(5))

# using the lambda function
print("Using lambda function, cube:", lambda_cube(5))




# Example 2: Python Lambda Function with List Comprehension
is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]

# iterate on each lambda function
# and invoke the function to get the calculated value
for item in is_even_list:
    print(item())






# Example 3: Example of lambda function using if-else
Max = lambda a, b: a if (a > b) else b

print(Max(1, 2))






# Example 4: Python Lambda with Multiple statements
List = [[2, 3, 4], [1, 4, 16, 64], [3, 6, 9, 12]]

# Sort each sublist
sortList = lambda x: (sorted(i) for i in x)

# Get the second largest element
secondLargest = lambda x, f: [y[len(y) - 2] for y in f(x)]
res = secondLargest(List, sortList)

print(res)




# Using lambda() Function with filter()
# Example 1: Filter out all odd numbers using filter() and lambda function
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)






# Example 2: Filter all people having age more than 18, using lambda and filter() function
# Python 3 code to people above 18 yrs
ages = [13, 90, 17, 59, 21, 60, 5]

adults = list(filter(lambda age: age > 18, ages))

print(adults)






# Using lambda() Function with map()
# Example 1: Multiply all elements of a list by 2 using lambda and map() function
# Python code to illustrate
# map() with lambda()
# to get double of a list.
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(map(lambda x: x * 2, li))
print(final_list)







# Example 2: Transform all elements of a list to upper case using lambda and map() function
# Python program to demonstrate
# use of lambda() function
# with map() function
animals = ['dog', 'cat', 'parrot', 'rabbit']

# here we intend to change all animal names
# to upper case and return the same
uppered_animals = list(map(lambda animal: animal.upper(), animals))

print(uppered_animals)



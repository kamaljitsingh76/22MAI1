# python code to demonstrate working of reduce()

# importing functools for reduce()
import functools

# initializing list
lis = [1, 3, 5, 6, 2, ]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a + b, lis))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))

# python code to demonstrate working of reduce()
# using operator functions

# importing functools for reduce()
import functools

# importing operator for operator functions
import operator

# initializing list
lis = [1, 3, 5, 6, 2, ]

# using reduce to compute sum of list
# using operator functions
print("The sum of the list elements is : ", end="")
print(functools.reduce(operator.add, lis))

# using reduce to compute product
# using operator functions
print("The product of list elements is : ", end="")
print(functools.reduce(operator.mul, lis))

# using reduce to concatenate string
print("The concatenated product is : ", end="")
print(functools.reduce(operator.add, ["geeks", "for", "geeks"]))

# python code to demonstrate summation
# using reduce() and accumulate()

# importing itertools for accumulate()
import itertools

# importing functools for reduce()
import functools

# initializing list
lis = [1, 3, 4, 10, 4]

# printing summation using accumulate()
print("The summation of list using accumulate is :", end="")
print(list(itertools.accumulate(lis, lambda x, y: x + y)))

# printing summation using reduce()
print("The summation of list using reduce is :", end="")
print(functools.reduce(lambda x, y: x + y, lis))


# Python program to  illustrate sum of two numbers.
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value


# Note that the initializer, when not None, is used as the first value instead of the first value from iterable , and after the whole iterable.
tup = (2, 1, 0, 2, 2, 0, 0, 2)
print(reduce(lambda x, y: x + y, tup, 6))








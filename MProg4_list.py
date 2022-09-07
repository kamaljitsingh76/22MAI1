# LIST - A list stores a series of items in a particular order. You
# access items using an index, or within a loop.

# Make a list
users = ['val', 'bob', 'mia', 'ron', 'ned']
print(users)
# Get the first item in a list
first_user = users[0]
print("Get the first item in a list users[0]-", first_user)
# Get the last item in a list
last_user = users[-1]
print("Get the last item in a list bikes[-1]-", last_user)

# Changing an element
users = ['val', 'bob', 'mia', 'ron', 'ned']
print("Elements of the users list before changing - ", users)
users[0] = 'valerie'
users[-2] = 'ronald'
print("Elements of the users list after changing users[0] and users[-2] - ", users)

# Looping through a list
for user in users:
    print(user)
# Adding items to a list
userA = []
print("Empty List bikesA before Adding items - ",userA)
userA.append('val')
userA.append('bob')
userA.append('mia')
print("List userA after Adding items - ",userA)

#Inserting elements at a particular position
userA.insert(0, 'joe')
userA.insert(3, 'bea')
print("List userA after inserting items - ",userA)

# Deleting an element by its position
del userA[-1]
print("List userA after deleting current element - ",userA)

#Removing an item by its value
userA.remove('joe')
print("List userA after removes item('joe') - ",userA)

#Slicing a list
first_two = users[:2]
print("slicing first two elements from users List = ", first_two)

#Copying a list
print("users list = ", users)
copy_of_users = users[:]
print("Copying List from users list = ", copy_of_users)

# Pop the last item from a list
most_recent_user = users.pop()
print("most_recent_user from users using pop() - ", most_recent_user)

#Pop the first item in a list
first_user = users.pop(0)
print("first_user from users using pop(0) - ",first_user)

#Find the length of a list
num_users = len(users)
print("We have " + str(num_users) + "in users list.")

#Sorting a list permanently
users.sort()
# Sorting a list permanently in reverse alphabetical order
users.sort(reverse=True)
# Sorting a list temporarily
print(sorted(users))
print(sorted(users, reverse=True))
# Reversing the order of a list
users.reverse()
#Printing all items in a list
for user in users:
    print(user)
# Printing a message for each item, and a separate message afterwards
for user in users:
    print("Welcome, " + user + "!")

print("Welcome, we're glad to see you all!")
# Making numerical lists
squares = []
for x in range(1, 11):
    squares.append(x**2)
print(squares)
# List comprehensions
squares = [x**2 for x in range(1, 11)]

# Printing the numbers 0 to 1000
for number in range(1001):
    print(number)
# Printing the numbers 1 to 1000
for number in range(1, 1001):
    print(number)
# Making a list of numbers from 1 to a million
numbers = list(range(1, 1000001))
print(numbers)

# Finding the minimum value in a list
ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
youngest = min(ages)
print("Youngest element in list is - ", youngest)

#Finding the maximum value
ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
oldest = max(ages)
print("Oldest element in list is - ", oldest)
#Finding the sum of all values
ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
total_years = sum(ages)
print("Total age in all element in list is - ", total_years)

# Using a loop to convert a list of names to upper case
names = ['kai', 'abe', 'ada', 'gus', 'zoe']
print(names)
upper_names = []
for name in names:
    upper_names.append(name.upper())
print("Names after Upper Case - ",upper_names)

# Using a comprehension to convert a list of names to upper case
names = ['kai', 'abe', 'ada', 'gus', 'zoe']
print("Before Upper Case = ",names)

upper_names = [name.upper() for name in names]
print("Names after Upper Case - ",upper_names)


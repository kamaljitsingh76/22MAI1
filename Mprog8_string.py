
#1 defining strings in Python
# all of the following are equivalent
my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello
                    WORLD'''
print(my_string)

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
        the world of Python"""
print(my_string)

#2 Accessing string characters in Python
str = 'programiz'
print('str = ', str)

#first character
print('str[0] = ', str[0])

#last character
print('str[-1] = ', str[-1])

#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])

#slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])

# index must be in range
#my_string[15]

#IndexError: string index out of range

# index must be an integer
#my_string[1.5] 

#TypeError: string indices must be integers

#3  Python String Operations
str1 = 'Hello '
str2 ='World!'

# using +
print('str1 + str2 = ', str1 + str2)

# using *
print('str1 * 3 =', str1 * 3)

# two string literals together
print('Hello ''World!')

# Iterating through a string
count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1
print(count,'letters found')

str = 'cold'

# enumerate()
list_enumerate = list(enumerate(str))
print('list(enumerate(str) = ', list_enumerate)

#character count
print('len(str) = ', len(str))

print("PrOgRaMiZ".lower())

print("PrOgRaMiZ".upper())

print("This will split all words into a list".split(' '))

print(' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string']))

print('Happy New Year'.find('ew'))

print('Happy New Year'.replace('Happy','Brilliant'))

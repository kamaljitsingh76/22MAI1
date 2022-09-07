a=()
print(a)
print(type(a))

print(type(()))
t = (23, 'abc', 4.56, (2,3), 'def')
print(t[-3])

li = list(t)
print(li[3])

tu = tuple(li[1:4])
print(tu)
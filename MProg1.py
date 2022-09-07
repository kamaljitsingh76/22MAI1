listA=["apple","banana","cherry","grapes"]
print(listA)
"""
thisList.append("grapes")
print(thisList)
print(len(thisList))
print(type(thisList))
"""
listB=list((10,5,4))
listA.extend(listB)
print(listA)

print(listA[2:6])
if 10 in listA:
    print('10 is present in list')


listA.insert(1,'grapes')
print(listA)

"""listA.remove('grapes')"""
print(listA.count('grapes'))

listA.reverse()

print(listA)
listB=list((10,5,4))
print(listB)
listB.sort()

print(listB)
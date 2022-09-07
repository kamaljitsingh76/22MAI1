"""

for i in range(1,11,1):
    if(i == 5 or i == 8):
        continue
    print(i, end=" ")
"""







str1=str(input("Please Enter the String: "))
print(" Entered String is : ", str1)
print(" After Removing Spaces, the String becomes:")
for i in str1:
    if i==" ":
        continue
    print(i, end="")
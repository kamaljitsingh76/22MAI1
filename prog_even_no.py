sum=0
print("Even numbers from 0 to 10 are as follows")
for i in range(0,11,1):
    if i%2==0:
        print(i)
        sum=sum+i
print("Sum of Even numbers from 0 to 10 is = ", sum)
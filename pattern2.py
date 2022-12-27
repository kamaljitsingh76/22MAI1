a=1
b=0
c=0
n=int(input("enter the value of n"))
for x in range(0,n):
    for y in range(0,n-x-1):
        print(" ",end ='')
    for z in range(0,2*x+1):
        c=a+b
        a=b
        b=c
        print(c,end='')
    print("\n")

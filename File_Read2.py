#open the file.txt in read mode. causes an error if no such file exists.
fileptr = open("file2.txt","r");
#print(fileptr[0:21])
#running a for loop
count=0
for i in fileptr:
    for j in i:
        
    print(i) # i contains each line of the file


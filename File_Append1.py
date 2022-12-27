# open the file.txt in append mode. Create a new file if no such file exists.
fileptr = open("file2.txt", "a")

# appending the content to the file
fileptr.write('''Python is the modern day language. It makes things so simple. 
It is the fastest-growing programing language This is Additional''')

# closing the opened the file
fileptr.close()

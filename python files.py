'''file1 = open("text.txt", "r")
data = file1.read()
print(data)
file1.close()

file2 = open("text.txt", "w")
str1 = 'Python'
print(file2.write(str1))
file2.close()

file3 = open("text.txt", "a")
str1 = 'Python'
print(file3.write(str1))
file3.close()

file3 = open("text.txt", "r+")
print(file3.readline(11))
print()'''

'''with open('text.txt') as f:
    contents = f.read()
    print(contents)'''

'''with open('text.txt') as f:
    [print(line) for line in f.readlines()]'''


'''file1 = open("text.txt", "r")
data = file1.readlines(5)
print(data)
file1.seek(0)
data = file1.read()
print(data)
file1.close()'''

import os
print(os.access('text.txt', os.R_OK))  # Check for read access
print(os.access('text.txt', os.W_OK))  # Check for write access
print(os.access('text.txt', os.X_OK))  # Check for execution access
print(os.access('text.txt', os.F_OK))  # Check for existance of file

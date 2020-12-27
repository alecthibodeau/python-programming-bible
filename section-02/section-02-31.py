# Section 2
# 31. File Inputs & Outputs

import os

print("Hello World")

# User input argument
# var1 = input("Enter something please: ")
# print(var1)

# Open file with read-only "r" argument
# var2 = open("File.txt", "r")

# Open file with writable binary "wb" argument,
# which creates a new file if it doesn't exist
# var2 = open("File.txt", "wb")

# Open file with writable "w" argument
# var2 = open("File.txt", "w")

# Open file as readable and writable "r" argument
# var2 = open("File.txt", "r+")

# Open file with append "a" argument
# var2 = open("File.txt", "a")

# Open file with writable "w" argument
var2 = open("File.txt", "w")
print(var2)
print(var2.name)

# Writing to the file
var2.write("Hello my name is Bob")
var2.close

var2 = open("File.txt", "r")

# Reading the file
string1 = var2.read(10) # specify number of bytes to be read from the open file
print(string1)

# Close file
var2.close

os.rename("File.txt", "NewName.txt")
# os.remove("FileLocation and FileName")

os.mkdir("New Folder")

# Input and Output - https://docs.python.org/3/tutorial/inputoutput.html

# Output
# Hello World
# <_io.TextIOWrapper name='File.txt' mode='w' encoding='UTF-8'>
# File.txt
# Hello my n

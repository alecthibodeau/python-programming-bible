# Section 2
# 24. Strings

string1 = "Python is amazing"

print(string1)
print(string1[1])
print(string1[1:4])

# Reassign string variable
# string1 = "Jpij4"

print(string1[:4] + " Bob")

string2 = "Python is the best"

# Escape characters
print("Hello \n World") # new line escape character

# Concatenation
string3 = string1 + ' ' + string2
print(string3)

# Format Operator
var1 = "Hello"
var2 = "World"
print("%s this is the best %s" % (var1, var2))

# Triple Quotes (to place text on several lines)
lorem = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco
laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate
velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident,
sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
print(lorem)

# Built-in string methods https://developers.google.com/edu/python/strings

var4 = "hello world"
print(var4.capitalize()) # capitalize first character

# Output
# Python is amazing
# y
# yth
# Pyth Bob
# Hello
#  World
# Python is amazing Python is the best
# Hello this is the best World
# Lorem ipsum dolor sit amet,
# consectetur adipiscing elit, sed do eiusmod
# tempor incididunt ut labore et dolore magna aliqua.
# Ut enim ad minim veniam, quis nostrud exercitation ullamco
# laboris nisi ut aliquip ex ea commodo consequat.
# Duis aute irure dolor in reprehenderit in voluptate
# velit esse cillum dolore eu fugiat nulla pariatur.
# Excepteur sint occaecat cupidatat non proident,
# sunt in culpa qui officia deserunt mollit anim id est laborum.

# Hello world

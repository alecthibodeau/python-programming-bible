# Section 2
# 27. Dictionary in Depth

# Creating Dictionaries
dictionary1 = { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4 }

# Accessing Values
print(dictionary1)
print(dictionary1['a'])
print(dictionary1['d'])

# Updating Values
dictionary1['a'] = "Hello world"
print(dictionary1['a'])

# Deleting Values
del dictionary1['a']
print(dictionary1)

# Methods of List Objects — https://docs.python.org/3.6/tutorial/datastructures.html
print(len(dictionary1))

# Delete Entire Dictionary
dictionary1.clear()
del dictionary1

# Output
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# 1
# 4
# Hello world
# {'b': 2, 'c': 3, 'd': 4}
# 3

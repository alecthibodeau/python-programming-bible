# Section 2
# 26. Tuples in Depth

# Creating Tuples
tuple1 = (1, 2, 3, "a", "b", "c")

# Accessing Tuples
print(tuple1)
print(tuple1[1])
print(tuple1[0:4])

# Tuple Operations - Python Tuple https://www.programiz.com/python-programming/tuple
print(len(tuple1))

# Deleting Tuples
# You can delete an entire tuple, but not its individual elements
del tuple1
print(tuple1) # NameError: name 'tuple1' is not defined

# You can't update a tuple - "TypeError: 'tuple' object does not support item assignment"
# tuple1[0] = 5

# You can create a new tuple with the foundation of a previous tuple or multiple tuples

# Output
# (1, 2, 3, 'a', 'b', 'c')
# 2
# (1, 2, 3, 'a')
# 6

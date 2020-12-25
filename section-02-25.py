# Section 2
# 25. Lists in Depth

listNumber1 = [1, 2, 3, "Hello", "World", 4, 5, 6]

# Access
print(listNumber1)
print(listNumber1[2])

# Update
print(listNumber1[0])
listNumber1[0] = "Bob"
print(listNumber1[0])

# Delete
print(listNumber1)
del listNumber1[1]
print(listNumber1)

# Built-in list methods https://developers.google.com/edu/python/lists

print(len(listNumber1)) # get length
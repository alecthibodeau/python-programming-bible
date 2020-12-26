# Assert Statement
def Function1(var1):
    assert(var1 != 0), "Zero is invalid" # Assert what is valid and not valid
    return 10 / var1

print(Function1(5))
# print(Function1(0))

try:
    file = open("Text.txt", "w")
    file.write("Hello")
except IOError:
    print("File not found")
else:
    print("A OK")
    file.close()

# Errors and Exceptions — https://docs.python.org/3/tutorial/errors.html

# Output
# 2.0
# A OK

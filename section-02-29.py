# Section 2
# 29. Functions

varGlobal = 1

def AwesomeFunction():
    "This function is awesome"
    print("Hello World")
    print("My name is bob and no I cannot fix it")
    return

AwesomeFunction()
AwesomeFunction()
AwesomeFunction()

def AwesomeFunction2(number1, number2):
    "Adds the numbers together"
    return number1 + number2

print(AwesomeFunction2(5, 6))

var1 = 5
print(var1)

def ChangeFunction(number1):
    "Change function"
    number1 = 8 # A variable created inside a function is limited to local scope
    return

print(var1)

# Default argument that gets passed when no other argument is used
# Default arguments must be at the end
def DefaultArg(var1 = 8):
    return var1 * 2

print(DefaultArg(9))
print(DefaultArg())

# Output
# Hello World
# My name is bob and no I cannot fix it
# Hello World
# My name is bob and no I cannot fix it
# Hello World
# My name is bob and no I cannot fix it
# 11
# 5
# 5
# 18
# 16

# Section 3
# 36. Constructor New & Init Method

class Vehicle:#(object):
    speed = 0

    # This is the constructor for Python, which you generally won't use
    def __new__(cls):
        return object.__new__(cls)

    # This is the initialization method, not the constructor
    # It's called after the class has been created and has access to all the variables and methods
    # Every time we create a class it'll call the constructor and then the intialization method
    def __init__(self, speed = 0):
        self.speed = speed # assigning to the local variable

    def IncreaseSpeed(self, increaseAmount):
        self.speed += increaseAmount

car1 = Vehicle()
car2 = Vehicle(89)

print("Speed for car 1: %i" % (car1.speed))
print("Speed for car 2: %i" % (car2.speed))
car1.IncreaseSpeed(5)
print("Speed for car 1: %i" % (car1.speed))
print("Speed for car 2: %i" % (car2.speed))

# Output
# Speed for car 1: 0
# Speed for car 2: 89
# Speed for car 1: 5
# Speed for car 2: 89

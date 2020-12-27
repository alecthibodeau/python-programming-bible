# Section 3
# 41. Overloading Operators

# Python Operator Overloading - https://thepythonguru.com/python-operator-overloading/

class Vehicle:#(object):
    speed = 0

    # This is the constructor for Python, which you generally won't use
    # def __new__(cls):
    #     return object.__new__(cls)

    # This is the initialization method, not the constructor
    # It's called after the class has been created and has access to all the variables and methods
    # Every time we create a class it'll call the constructor and then the intialization method
    # For any default method of a class (init, delete, destructor, object comparison, etc.)
    # we can overload it - meaning we can change the default functionality,
    # which is what we're doing here:
    def __init__(self, speed = 0):
        self.speed = speed # assigning to the local variable

    def IncreaseSpeed(self, increaseAmount):
        self.speed += increaseAmount

    # When we add car1 and car2 this overloaded operator is invoked,
    # And as a result we create a new Vehicle object, which gets returned and assigned 'car3'
    # We are passing in the speeds from both objects (car1 and car2) and adding them together
    # And because our init method allows us to set a new value for speed, this becomes the new speed
    def __add__(self, otherVehicle):
        return Vehicle(self.speed + otherVehicle.speed)

    def __del__(self):
        print("Object has been destroyed")

class Car(Vehicle): # Car class is inheriting from Vehicle
    weight = 10

    def IncreaseWeight(self, weight):
       self.weight += weight

    def IncreaseSpeed(self, increaseAmount):
        self.speed *= increaseAmount

car1 = Vehicle()
car2 = Vehicle(89)
# Speed is set to 5 on creating childCar
childCar = Car(5)

print(childCar.weight)
childCar.IncreaseWeight(9)
print(childCar.weight)
# Increase speed in the child class, not the parent class, which multiplies rather than adds
childCar.IncreaseSpeed(5)
print(childCar.speed)

print("Speed for car 1: %i" % (car1.speed))
print("Speed for car 2: %i" % (car2.speed))
car1.IncreaseSpeed(5)
print("Speed for car 1: %i" % (car1.speed))
print("Speed for car 2: %i" % (car2.speed))

car3 = car1 + car2
print("Speed for car 3: %i" % (car3.speed))

del car1

# Output
# 10
# 19
# 25
# Speed for car 1: 0
# Speed for car 2: 89
# Speed for car 1: 5
# Speed for car 2: 89
# Speed for car 3: 94
# Object has been destroyed
# Object has been destroyed
# Object has been destroyed
# Object has been destroyed

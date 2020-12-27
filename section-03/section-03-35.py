# Section 3
# 35. Accessing Attributes

class Vehicle:
    speed = 0

    def IncreaseSpeed(self, increaseAmount):
        self.speed += increaseAmount

car1 = Vehicle()
car2 = Vehicle()

print("Speed for car 1: %i" % (car1.speed))
car1.IncreaseSpeed(5)
print("Speed for car 1: %i" % (car1.speed))
print("Speed for car 2: %i" % (car2.speed))

# Output
# Speed for car 1: 0
# Speed for car 1: 5
# Speed for car 2: 0

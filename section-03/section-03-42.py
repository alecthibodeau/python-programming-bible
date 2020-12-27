# Section 3
# 42. Data Hiding

class Vehicle:
    __speed = 0

    def __init__(self, speed = 0):
        self.__speed = speed

car1 = Vehicle(5)

# print(car1.speed) # this won't work because the data is hidden

# We can access it this way, which is not recommended
# Use getters and setters instead
print(car1._Vehicle__speed)

# Output
# 5

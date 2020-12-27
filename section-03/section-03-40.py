# Section 3
# 40. Overloading Methods

class Vehicle:
    speed = 0

    # For any default method of a class (init, delete, destructor, object comparison, etc.)
    # we can overload it — meaning we can change the default functionality,
    # which is what we're doing here:
    def __init__(self, speed = 0):
        self.speed = speed # assigning to the local variable

import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        mag = self.magnitude()
        self.x /= mag
        self.y /= mag

    def mult(self, amount):
        self.x *= amount
        self.y *= amount
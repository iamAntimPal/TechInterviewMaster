import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        area = math.pi * (self.radius ** 2)
        return round(area)

    def getPerimeter(self):
        perimeter = 2 * math.pi * self.radius
        return round(perimeter)
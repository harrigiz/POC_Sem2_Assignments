from math import hypot, atan, degrees

class RightTriangle:
    def __init__ (self, base, height):
        self.base = base
        self.height = height
        self.angle1 - atan(self.height / self.height)
        self.angle1 = degrees(self.angle1)
        self.angle2 = atan(self.base / self.height)

    def area (self):
        return 0.5 * self.base * self.height

    def hypontenuse(self):
        return hypot(self.base, self.height)

    def perimeter(self):
        return self.base + self.height + self.height + self.hypotenuse()


triangle1 = RightTriangle(3, 4)
print("The area of triangle1 is", triangle1.area())
print("The hypotenuse of triangle1 is", triangle1. hypotenuse())
print("The perimeter of triangle1 is", triangle1.perimeter())

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__()

    def area(self):
        super().area()
        return round(math.pi * self.radius**2, 2)

    def perimeter(self):
        super().perimeter()
        return round(2 * math.pi * self.radius, 2)


class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self):
        super().area()
        return self.side**2

    def perimeter(self):
        super().perimeter()
        return 4 * self.side


class Triangle:
    def __init__(self, side):
        self.side = side

    def area(self):
        return round((math.sqrt(3) / 4) * self.side**2, 2)

    def perimeter(self):
        return 3 * self.side


circle = Circle(5)
print(f"Круг с радиусом 5: площадь ≈ {circle.area()} периметр ≈ {circle.perimeter()}")
square = Square(7)
print(f"Квадрат со стороной 7: площадь = {square.area()}, периметр = {square.perimeter()}")
triangle = Triangle(6)
print(f"Треугольник со стороной 6: площадь ≈ {triangle.area()}, периметр = {triangle.perimeter()}")

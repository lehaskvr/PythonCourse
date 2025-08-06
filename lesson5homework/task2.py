from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def get_shape_info(self):
        print(f"Тип фигуры: {self._name}")
        print(f"Периметр: {self.perimeter()}")
        print(f"Площадь: {self.area()}")

    @staticmethod
    def compare_areas(a: "Shape", b: "Shape"):
        area1 = a.area()
        area2 = b.area()
        if area1 > area2:
            return 1
        elif area1 < area2:
            return 2
        else:
            return 0


class Circle(Shape):
    def __init__(self, radius):
        self._name = "Круг"
        if radius > 0:
            self._radius = radius
        else:
            raise ValueError("Радиус не может быть отрицательным")

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        if new_radius > 0:
            self._radius = new_radius
        else:
            raise ValueError("Радиус не может быть отрицательным")

    def area(self):
        return round(math.pi * self._radius**2, 2)

    def perimeter(self):
        return round(2 * math.pi * self._radius, 2)

    def get_shape_info(self):
        super().get_shape_info()
        print(f"Радиус круга: {self._radius}")


class Square(Shape):
    def __init__(self, side):
        self._name = "Квадрат"
        if side > 0:
            self._side = side
        else:
            raise ValueError("Сторона не может быть отрицательной")

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, new_side):
        if new_side > 0:
            self._side = new_side
        else:
            raise ValueError("Сторона не может быть отрицательной")

    def area(self):
        return self._side**2

    def perimeter(self):
        return 4 * self._side

    def get_shape_info(self):
        super().get_shape_info()
        print(f"Сторона квадрата: {self._side}")


class Triangle(Shape):
    def __init__(self, side):
        self._name = "Треугольник"
        if side > 0:
            self._side = side
        else:
            raise ValueError("Сторона не может быть отрицательной")

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, new_side):
        if new_side > 0:
            self._side = new_side
        else:
            raise ValueError("Сторона не может быть отрицательной")

    def area(self):
        return round((math.sqrt(3) / 4) * self._side**2, 2)

    def perimeter(self):
        return 3 * self._side

    def get_shape_info(self):
        super().get_shape_info()
        print(f"Сторона треугольника: {self._side}")


circle = Circle(5)
print(f"Круг с радиусом 5: площадь ≈ {circle.area()} периметр ≈ {circle.perimeter()}")
square = Square(7)
print(
    f"Квадрат со стороной 7: площадь = {square.area()}, периметр = {square.perimeter()}"
)
triangle = Triangle(6)
print(
    f"Треугольник со стороной 6: площадь ≈ {triangle.area()}, периметр = {triangle.perimeter()}"
)
print(Circle.compare_areas(circle, square))
circle.get_shape_info()
square.get_shape_info()
triangle.get_shape_info()

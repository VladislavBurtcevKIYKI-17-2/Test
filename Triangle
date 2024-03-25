import math

class ShapeCalculator:
    @staticmethod
    def circle_area(radius):
        if radius < 0:
            raise ValueError("Радиус не может быть отрицательным")
        return math.pi * radius**2

    @staticmethod
    def triangle_area(side1, side2, side3):
        if side1 < 0 or side2 < 0 or side3 < 0:
            raise ValueError("Длины сторон не могут быть отрицательными")
        s = (side1 + side2 + side3) / 2
        area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
        return area

# Пример использования библиотеки
radius = 5
circle_area = ShapeCalculator.circle_area(radius)
print(f"Площадь круга с радиусом {radius}: {circle_area}")

side1, side2, side3 = 5, 7, 8
triangle_area = ShapeCalculator.triangle_area(side1, side2, side3)
print(f"Площадь треугольника со сторонами {side1}, {side2}, {side3}: {triangle_area}")

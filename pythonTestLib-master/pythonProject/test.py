import unittest
from math import pi
from area import Area


class TestShapeCalculator(unittest.TestCase):
    def test_circle_area(self):
        # Проверка вычисления площади круга
        area_calculator = Area()
        circle = area_calculator.circle_area(5)
        self.assertEqual(circle, pi * 5 ** 2)
        circle = area_calculator.circle_area(10)
        self.assertEqual(circle, pi * 10 ** 2)
        circle = area_calculator.circle_area(-5)
        self.assertEqual(circle, "Ошибка. Радиус не может быть отрицательным.")

    def test_triangle_area(self):
        # Проверка вычисления площади треугольника
        area_calculator = Area()
        triangle = area_calculator.triangle_area(3, 4, 5)
        self.assertEqual(triangle, [6.0, True])
        area_calculator = Area()
        triangle = area_calculator.triangle_area(4, 8, 9)
        self.assertEqual(triangle, [15.998046755776157, False])
        area_calculator = Area()
        triangle = area_calculator.triangle_area(-3, 4, 5)
        self.assertEqual(triangle, "Ошибка. Стороны не могут быть отрицательными или нулевыми.")


if __name__ == "__main__":
    unittest.main()

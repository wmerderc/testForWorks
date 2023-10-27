from math import sqrt, pi


class Area:
    @staticmethod
    def triangle_area(a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            return "Ошибка. Стороны не могут быть отрицательными или нулевыми."
        rectangular = False
        if a != b and a != c and b != c:
            if (b * b + c * c) == (a * a) or (a * a + b * b) == (c * c) or (a * a + c * c) == (b * b):
                # По теореме Пифагора проверяем является ли прямоугольным.
                rectangular = True

        p = (a + b + c) / 2
        s = sqrt(p * (p - a) * (p - b) * (p - c))
        return [s, rectangular]
        # Возвращаем массив с 2 значениями. Первое площадь, второе является ли прямоугольным.

    @staticmethod
    def circle_area(r):
        if r < 0:
            return "Ошибка. Радиус не может быть отрицательным."
        return pi * r ** 2

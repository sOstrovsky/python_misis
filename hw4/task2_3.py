import math

from pythonProject.hw4.task1 import Point


def get_length(p1, p2):
    return math.sqrt((p1.get_x() ** 2 - p2.get_x() ** 2) + (p1.get_y() ** 2 - p2.get_y() ** 2))


class Rectangle:
    def __init__(self, left_bottom_corner: Point, right_top_corner: Point):
        self.__left_bottom_corner = left_bottom_corner
        self.__right_top_corner = right_top_corner

    def __str__(self):
        return f'Rectangle: LBC: {self.__left_bottom_corner} and RTC: {self.__right_top_corner}'

    def get_perimeter(self):
        ltc = Point(self.__left_bottom_corner.get_x(), self.__right_top_corner.get_y())
        rbc = Point(self.__right_top_corner.get_x(), self.__left_bottom_corner.get_y())
        lbc = self.__left_bottom_corner
        rtc = self.__right_top_corner
        l_side = get_length(ltc, lbc)
        r_side = get_length(rtc, rbc)
        t_side = get_length(rtc, ltc)
        b_side = get_length(rbc, lbc)
        return round(l_side + r_side + t_side + b_side, 2)

    def get_area(self):
        ltc = Point(self.__left_bottom_corner.get_x(), self.__right_top_corner.get_y())
        lbc = self.__left_bottom_corner
        rtc = self.__right_top_corner
        l_side = get_length(ltc, lbc)
        t_side = get_length(rtc, ltc)
        return round(l_side * t_side, 2)

    def contains(self, p: Point):
        ltc = Point(self.__left_bottom_corner.get_x(), self.__right_top_corner.get_y())
        rbc = Point(self.__right_top_corner.get_x(), self.__left_bottom_corner.get_y())
        lbc = self.__left_bottom_corner
        return lbc.get_x() <= p.get_x() <= rbc.get_x() and lbc.get_y() <= p.get_y() <= ltc.get_y()


def print_result():
    x1, y1 = map(int, input('Введите координаты левого нижнего угла через пробел: ').split())
    x2, y2 = map(int, input('Введите координаты правого верхнего угла через пробел: ').split())

    r = Rectangle(Point(x1, y1), Point(x2, y2))

    print(f'Периметр прямоугольника: {r.get_perimeter()}')
    print(f'Площадь прямоугольника: {r.get_area()}')

    x3, y3 = map(int, input('Введите координаты произвольной точки: ').split())
    print(r.contains(Point(x3, y3)))

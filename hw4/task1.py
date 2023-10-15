class Point:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'Point({self.__x}, {self.__y})'

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y


def print_result():
    x = int(input('Введите координату \'x\': '))
    y = int(input('Введите координату \'y\': '))

    p = Point(x, y)
    print(p)

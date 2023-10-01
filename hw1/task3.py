def get_cube_root(n):
    return n ** (1. / 3.)


def get_result(x, y, z):
    numerator = (x ** 5 + 7) / (abs(-6) * y)
    return round(get_cube_root(numerator) / (7 - z % y), 3)


def print_result():
    x = int(input('Введите число \'x\': '))
    y = int(input('Введите число \'y\': '))
    z = int(input('Введите число \'z\': '))
    print(get_result(x, y, z))

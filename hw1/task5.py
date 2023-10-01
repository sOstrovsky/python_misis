def print_result():
    _range = [int(input('Введите левую границу отрезка: ')), int(input('Введите правую границу отрезка: '))]
    a = int(input('Введите число \'a\': '))
    b = int(input('Введите число \'b\': '))
    print(is_solution_in_range(_range, a, b))


def is_solution_in_range(_range, a, b):
    if a == 0:
        return b == 0 and _range[0] <= 0 <= _range[1]

    x = -b / a

    return _range[0] <= x <= _range[1]

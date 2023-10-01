import math


def get_count(number):
    s = str(number)
    if '.' in s:
        return abs(s.find('.') - len(s)) - 1
    else:
        return 0


def run_math(a, b):
    return {
        'Сумма чисел': a + b,
        'Разница чисел': a - b,
        'Произведение чисел': a * b,
        'Результат деления \'a\' на \'b\'': a / b,
        'Результат целочисленного деления \'a\' на \'b\'': a // b,
        'Остаток от деления \'a\' на \'b\' по модулю': a % b,
        'Результат возведения \'a\' в степень \'b\'': a % b,
        'Десятичный логарифм \'a\'': math.log10(a),
        'Десятичный логарифм \'b\'': math.log10(b),
        '\'a < b\'': a < b,
        '\'a <= b\'': a <= b,
        '\'a > b\'': a > b,
        '\'a >= b\'': a >= b,
        '\'a != b\'': a != b,
        '\'a == b\'': a == b,
    }


def print_result():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    results = run_math(a, b)

    for key in results:
        result = results[key]
        print(f'{key}: ', result if get_count(result) <= 2 else round(result, 2))

def nok(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)


def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def print_result():
    x = int(input('a = '))
    y = int(input('b = '))
    print('НОК:', nok(x, y))
    print('НОД:', nod(x, y))

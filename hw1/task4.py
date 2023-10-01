def get_resistance(r1, r2):
    return f'{(r1 + r2):.1f}'


def print_result():
    r1 = int(input('Введите сопротивление первого проводника: '))
    r2 = int(input('Введите сопротивление второго проводника: '))

    print(get_resistance(r1, r2))

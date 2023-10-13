def bin_to_target(n, target):
    to_ten = int(n, 2)
    if target == '10':
        return to_ten
    elif target == '8':
        return oct(to_ten)
    elif target == '16':
        return hex(to_ten)


def eigths_to_target(n, target):
    to_ten = int(n, 8)
    if target == '10':
        return to_ten
    elif target == '2':
        return bin(to_ten)
    elif target == '16':
        return hex(to_ten)


def ten_to_target(n, target):
    if target == '2':
        return bin(n)
    elif target == '8':
        return oct(n)
    elif target == '16':
        return hex(n)


def sixteenth_to_target(n, target):
    to_ten = int(n, 16)
    if target == '10':
        return to_ten
    elif target == '2':
        return bin(to_ten)
    elif target == '8':
        return oct(to_ten)


def print_result():
    syst_start = input(' Введите исходную систему счисления(2, 8, 10, 16): ')
    syst_target = input(' Введите исходную систему счисления(2, 8, 10, 16): ')
    n = input(' Введите число для преобразования: ')
    if syst_start == '2':
        print(bin_to_target(n, syst_target))
    if syst_start == '8':
        print(eigths_to_target(n, syst_target))
    if syst_start == '10':
        print(ten_to_target(int(n), syst_target))
    if syst_start == '16':
        print(sixteenth_to_target(n, syst_target))

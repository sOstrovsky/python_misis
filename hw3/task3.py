def print_result():
    sym = '$'
    s = input('Введите текст: ')

    lng = len(s) + 2
    print(sym * lng)
    print(f'{sym}{s}{sym}')
    print(sym * lng)

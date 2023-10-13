def is_string_with_digit(s):
    for i in s:
        if i.isdigit():
            return True
    return False


def print_result():
    data = ['skdjhg ksdjha 2',
            'skdjhg ksdjha',
            'skdjhg ksdj4ha 2',
            '4skdjhg ksdjha',
            'skd4jhg ksdjha',
            'skdjhg ksdjha']

    cnt = 0

    for i in data:
        if is_string_with_digit(i):
            cnt += 1

    print(f'Строк с цифрой: {cnt}')

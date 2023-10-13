def get_missed_nums(data):
    if data == list(reversed(data)):
        print('Последовательность симметрична')
        return 0
    idx = 0
    to_add = [data[idx]]

    while data + to_add != list(reversed(data + to_add)):
        idx += 1
        to_add.insert(0, data[idx])
    return to_add


def print_result():
    n = int(input('Введите кол-во чисел: '))
    data = []
    for i in range(n):
        num = int(input(f'Число {i + 1}: '))
        data.append(num)
    result = get_missed_nums(data)
    if result:
        print(f'Последовательность: {data}')
        print(f'Нужно приписать чисел: {len(result)}')
        print(f'Сами числа: {list(reversed(result))}')

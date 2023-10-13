def get_debt_info():
    to = int(input('Кому? '))
    who = int(input('От кого? '))
    amount = int(input('Сумма: '))
    return [to, who, amount]


def get_totals(data, n):
    result = {i + 1: 0 for i in range(n)}
    for to, who, amount in data:
        result[to] -= amount
        result[who] += amount
    return result


def print_result():
    n = int(input('Введите кол-во друзей: '))
    k = int(input('Введите кол-во долговых расписок: '))

    data = []
    for i in range(k):
        print(f'{i + 1}-я расписка')
        data.append(get_debt_info())

    total = get_totals(data, n)
    print('Баланс друзей:')
    for i in total:
        print(f'{i}: {total[i]}')

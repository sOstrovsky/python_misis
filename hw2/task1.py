a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]


def print_result():
    a.extend(b)
    cnt1 = a.count(5)
    print(f'Кол-во цифр 5 при первом объединении: {cnt1}')
    for _ in range(cnt1):
        a.remove(5)
    a.extend(c)
    cnt2 = a.count(3)
    print(f'Кол-во цифр 3 при втором объединении: {cnt2}')
    print('Итоговый список:', a)

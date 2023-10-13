def get_max_count(n, k):
    res = 0

    for i in range(len(k)):
        for j in k:
            if len(k) and i + 1 <= len(n):
                if n[i] >= j:
                    res += 1
                    k.remove(j)
                    break
    return res


def print_result():
    count_of_skates = int(input('Кол-во коньков: '))
    skates, sizes = [], []
    for i in range(count_of_skates):
        skates.append(int(input(f'Размер {i + 1}-й пары: ')))

    count_of_people = int(input('Кол-во людей: '))
    for i in range(count_of_people):
        sizes.append(int(input(f'Размер ноги {i + 1}-го человека: ')))

    print(f'Наибольшее кол-во людей, которые могут взять ролики: {get_max_count(skates, sizes)}')

def get_stats(s):
    res = {}
    for i in s:
        li = i.lower()
        if li in res:
            res[li] = res[li] + 1
        else:
            res[li] = 1
    return res


def print_result():
    s = input('Введите текст: ')
    stats = get_stats(s)
    for key in stats:
        print(f'{key}: {stats[key]}')

def sort_nums(a, b, c):
    min_n = min(a, b, c)
    max_n = max(a, b, c)
    sum_n = a + b + c
    return min_n, sum_n - min_n - max_n, max_n


def print_result():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    c = int(input('Введите третье число: '))

    print(sort_nums(a, b, c))

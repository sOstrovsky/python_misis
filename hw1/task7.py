def get_mult(n):
    n_list = list(n)
    result = 1
    for x in n_list:
        result *= int(x)
    return result


def get_sum(n):
    n_list = list(n)
    result = 1
    for x in n_list:
        result += int(x)
    return result


def print_result():
    a = input('Введите двузначное число: ')
    b = input('Введите трехзначное число: ')
    print(get_mult(a), get_sum(a))
    print(get_mult(b), get_sum(b))

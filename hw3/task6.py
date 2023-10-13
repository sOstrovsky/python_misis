def create_tuple(*nums):
    positive = []
    negative = []
    for i in nums:
        if i >= 0:
            positive.append(i)
        else:
            negative.append(i)
    return (list(sorted(positive)), list(reversed(sorted(negative))))


def print_result():
    args = list(map(int, input('Введите положительные и отрицательные числа/цифры через пробел: ').split()))
    print(create_tuple(*args))

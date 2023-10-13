import math

max_n = 100
min_n = 1


def get_avg(a, b):
    return math.ceil((a + b) / 2)


def run_game(n):
    guess = get_avg(max_n, min_n)
    low = min_n
    high = max_n
    while n != guess:
        ask = int(input(f'Твое число равно, меньше или больше, чем число {guess}? (1 - больше, 2 - меньше, 3 - равно)'))
        if ask == 1:
            low = guess + 1
        elif ask == 2:
            high = guess - 1
        guess = (low + high) // 2
    print(f'Загаданное число - {guess}')


def print_result():
    n = int(input(f'Введите число от {min_n} до {max_n}: '))
    run_game(n)

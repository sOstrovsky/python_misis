def run_game(n, k):
    circle = [i + 1 for i in range(n)]

    start = 1
    while len(circle) > 1:
        print(f'Текущий круг людей: {circle}')
        print(f'Начало счёта с номера: {start}')
        will_leave = circle.index(k % len(circle) + circle.index(start)) if k % len(circle) > 0 else 0
        print(f'Выбывает человек под номером {circle[will_leave]}')
        print(' ')
        start = circle[will_leave] + 1 if circle[will_leave] > 0 else circle[1]

        circle.remove(circle[will_leave])
    else:
        print(f'Остался человек под номером {circle[0]}')


def print_result():
    n = int(input('Кол-во человек: '))
    k = int(input('Какое число в считалке? '))
    print(f'Значит, выбывает каждый {k}-й человек')
    print('---')

    run_game(n, k)

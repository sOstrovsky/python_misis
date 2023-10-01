track_length = 123


def get_kilometer(v, t):
    distance = v * t
    return distance % track_length


def print_result():
    v = int(input("Введите скорость спортсмена в км/ч: "))
    t = int(input("Введите время в часах: "))

    print(f'Спортсмен остановится на {get_kilometer(v, t)} километре')

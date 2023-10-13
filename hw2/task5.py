violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]


def print_result():
    count = int(input('Сколько песен выбрать? '))
    total = 0
    for i in range(count):
        song = input(f'Название {i + 1}-й песни: ')
        for [name, duration] in violator_songs:
            if song == name:
                total += duration
    print(f'Общее время звучания песен: {total} минуты')

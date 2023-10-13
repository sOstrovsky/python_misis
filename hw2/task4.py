guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']


def print_result():
    while True:
        print(f'Сейчас на вечеринке {len(guests)} человек: {guests}')
        update = input('Гость пришёл или ушёл? ')
        if update == 'пришел':
            new_guest = input('Имя гостя: ')
            if len(guests) < 6:
                guests.append(new_guest)
                print(f'Привет, {new_guest}!')
            else:
                print(f'Прости, {new_guest}, но мест нет.')
        elif update == 'ушел':
            guest_to_leave = input('Имя гостя: ')
            if guest_to_leave in guests:
                guests.remove(guest_to_leave)
                print(f'Пока, {guest_to_leave}!')
        elif update == 'Пора спать':
            print('Вечеринка закончилась, все легли спать.')
            break

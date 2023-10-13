from datetime import date, timedelta

start_date = date(1901, 1, 1)
end_date = date(2000, 12, 31)


def check_date(user_date):
    yy, mm, dd = user_date.split('-')
    return int(dd) * int(mm) == int(yy[2:])


def print_result():
    user_date = input('Введите дату в формате \'YYYY-MM-DD\': ')
    res = 'является' if check_date(user_date) else 'не является'
    print(f'Дата {user_date} {res} магической')

    delta = end_date - start_date

    print('Все магические даты 20 века:')
    for i in range(delta.days + 1):
        day = start_date + timedelta(days=i)
        if check_date(day.strftime('%Y-%m-%d')):
            print(day)

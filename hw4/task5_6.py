import datetime

max_h = 23
max_m_s = 59


class WrongTimeError(Exception):
    print(f'Неправильное значение, {Exception}')


def add_lead_zero(n) -> str:
    return f'{n if n > 10 else str(n).zfill(2)}'


def get_diff(n, m):
    print(n, m)
    return n % m if n > m else 0


class Watches:
    def __init__(self, h='00', m='00', s='00'):
        if int(h) > max_h or int(m) > max_m_s or int(s) > max_m_s:
            raise WrongTimeError
        else:
            self.__h = h
            self.__m = m
            self.__s = s

    def __add__(self, other: "Watches"):
        new_date = (datetime.timedelta(hours=int(self.__h), minutes=int(self.__m), seconds=int(self.__s))
                    + datetime.timedelta(hours=int(other.__h), minutes=int(other.__m), seconds=int(other.__s)))
        new_time = str(new_date).split(', ').pop()
        hh, mm, ss = new_time.split(':')
        self.__h = hh
        self.__m = mm
        self.__s = ss

    def add_one_hour(self, m=False, s=False):
        new_hrs_val = int(self.__h) + 1
        hrs_diff = get_diff(new_hrs_val, max_h)
        if hrs_diff > 0:
            self.__h = '00'
            if m:
                self.__m = '00'
            if s:
                self.__s = '00'
        else:
            self.__h = add_lead_zero(new_hrs_val)

    def add_one_minute(self, m=False):
        new_min_val = int(self.__m) + 1
        min_diff = get_diff(new_min_val, max_m_s)
        if min_diff > 0:
            self.__m = add_lead_zero(0)
            self.add_one_hour(m, True)
        else:
            self.__m = add_lead_zero(new_min_val)

    def add_one_second(self):
        new_sec_val = int(self.__s) + 1
        sec_diff = get_diff(new_sec_val, max_m_s)
        if sec_diff > 0:
            self.__s = add_lead_zero(0)
            self.add_one_minute(True)
        else:
            self.__s = add_lead_zero(new_sec_val)

    def __str__(self):

        return f'Время на часах - {self.__h}:{self.__m}:{self.__s}'


def print_result():
    hh, mm, ss = input('Введите время в формате \'HH:MM:SS\': ').split(':')

    watches = Watches(hh, mm, ss)
    print(watches)

    watches.add_one_second()
    print(watches)
    watches.add_one_second()
    print(watches)
    watches.add_one_second()
    print(watches)
    watches.add_one_second()
    print(watches)

    watches.add_one_minute()
    print(watches)
    watches.add_one_minute()
    print(watches)
    watches.add_one_minute()
    print(watches)
    watches.add_one_minute()
    print(watches)

    watches.add_one_hour()
    print(watches)
    watches.add_one_hour()
    print(watches)
    watches.add_one_hour()
    print(watches)
    watches.add_one_hour()
    print(watches)

    hh2, mm2, ss2 = input('Введите время в формате \'HH:MM:SS\': ').split(':')

    watches2 = Watches(hh2, mm2, ss2)

    watches + watches2
    print(watches)

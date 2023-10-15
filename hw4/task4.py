class TenCounter:
    def __init__(self):
        self.__cnt = 0

    def increment(self):
        self.__cnt += 1

    def decrement(self):
        if self.__cnt > 0:
            self.__cnt -= 1
        else:
            print('Счетчик не может быть меньше 0')

    def get_counter(self):
        return self.__cnt


def print_result():
    tc = TenCounter()
    tc.increment()
    print(tc.get_counter())
    tc.increment()
    print(tc.get_counter())
    tc.increment()
    print(tc.get_counter())
    tc.increment()
    print(tc.get_counter())
    tc.decrement()
    print(tc.get_counter())
    tc.decrement()
    print(tc.get_counter())
    tc.decrement()
    print(tc.get_counter())
    tc.decrement()
    tc.decrement()
    print(tc.get_counter())
    tc.increment()
    print(tc.get_counter())

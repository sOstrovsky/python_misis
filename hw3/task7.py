def is_palindrome(s):
    res = []
    for i in s:
        res.insert(0, i)
    return ''.join(res) == s


def print_result():
    s = input('Введите строку: ')
    print(is_palindrome(s))

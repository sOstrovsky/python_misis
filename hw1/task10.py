def print_result():
    name = input('Введите название футбольной команды: ')
    print(f'{name} - чемпион!')
    name_lower = name.lower()
    print(len(name) * '-')
    print('п' in name_lower)
    chars_list = list(name_lower)
    print(chars_list.count('а'))

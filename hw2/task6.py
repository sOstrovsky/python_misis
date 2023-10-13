def print_result():
    list1, list2 = [], []
    for i in range(3):
        list1.append(input(f'Введите {i+1}-е число для первого списка: '))
    for i in range(7):
        list1.append(input(f'Введите {i+1}-е число для второго списка: '))
    print({*list1, *list2})

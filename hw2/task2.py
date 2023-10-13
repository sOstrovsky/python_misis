def create_list(a, b, step):
    return list(range(a, b, step))


def print_result():
    a = create_list(160, 176, 2)
    b = create_list(162, 180, 3)
    print(sorted([*a, *b]))

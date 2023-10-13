shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]


def create_structured_data(raw):
    res = {}
    for k, v in raw:
        if k in res:
            res[k]['amount'] += 1
            res[k]['total'] += v
        else:
            res[k] = {'amount': 1, 'total': v}
    return res


def print_result():
    data = create_structured_data(shop)
    for i in data:
        print(f'Название детали - {i}')
        print(f'Кол-во деталей - {data[i]["amount"]}')
        print(f'Общая стоимость - {data[i]["total"]}')
        print('---')

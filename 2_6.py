params = ['наименование', 'цена', 'количество', 'ед.']
goods = [good for good in input('Введите товары через пробел ').split(' ')]
prices = [price for price in input('Введите цены соотв. товаров через пробел ').split(' ')]
cnt = [x for x in input('Введите количество соотв. товаров через пробел ').split(' ')]
items = [item for item in input('Введите единицы измерения соотв. товаров через пробел ').split(' ')]
d = []
a = 1
for i, j, k, l in zip(goods, prices, cnt, items):
    d1 = dict(zip(params, (i, j, k, l)))
    d.append((a, d1))
    a += 1
print(d)
analytics = dict(zip(params, [goods, prices, cnt, items]))
print(analytics)
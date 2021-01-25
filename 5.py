revenue = int(input('Выручка '))
costs = int(input('Издержки '))
if revenue > costs:
    profit = revenue - costs
    print('Фирма работает с прибылью')
    print(f'Прибыль {profit}')
    print(f'Рентабельность {profit/costs}')
    num_empl = int(input('Кол-во сотрудников: '))
    print(f'Прибыль на сотрудника {profit/num_empl}')
elif revenue == costs:
    print('Точка безубыточности')
else:
    print('Фирма работает с убытком')


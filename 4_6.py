from itertools import count
from itertools import cycle

start = int(input('Задание 1, введите число: '))
for el in count(start):
    if el > 1000:
        break
    else:
        print(el)

my_l = [float(x) for x in input('Задание 2, введите спиcок: ').split(' ')]
с = 0
for el in cycle(my_l):
    if с > 100:
        break
    else:
        print(el)
        с += 1

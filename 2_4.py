l = [word for word in input('Введите строку из слов через пробел ').split(' ')]
k = 1
for i in l:
    if len(i) > 10:
        print(k, i[:10])
    else:
        print(k, i)
    k += 1

with open('5_2.txt', 'r', encoding = 'utf-8') as f:
    k = 0
    for line in f:
        k += 1
        n_w = 0
        for w in line.split():
            n_w += 1
        print(f'Кол-во слов в строке {k} равно {n_w}')
    print(f'Кол-во строк {k}')


def sum_num():
    sum = 0
    while True:
        s = input('Введите строку ').split(' ')
        try:
            for x in s:
                if x == '$':
                    print(sum)
                    break
                else:
                    sum += int(x)
            if '$' in s:
                break
        except ValueError:
            print('Должны вводиться только числа или спецсимвол $: ')
            print(f'Сумма, введенная до этого момента {sum}')
            break

sum_num()

def division():
    a = int(input('Введите числитель: '))
    b = int(input('Введите знаменатель: '))
    try:
        print(a/b)
    except:
        print('Division by zero')

division()


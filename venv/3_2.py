def client(**data):
    for info, name in data.items():
        print(f'{info}: {name}', end = ' ')

client(name = 'Dmitrii', surname = 'Ivanov', year_birth = '1988', city = 'Smolensk',
             email = 'aaa@yandex.ru', tel = '+79999999999')
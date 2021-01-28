l = [int(i) for i in input('Введите список через пробел ').split(' ')]
i =1
if len(l) % 2 == 0:
    while i < len(l):
        l[i-1], l[i] = l[i], l[i-1]
        i+=2
else:
    while i < len(l)-1:
        l[i-1], l[i] = l[i], l[i-1]
        i+=2
print(l)


my_list = [8, 5, 3, 3, 2, 1]
new_rating = int(input('Введите новый рейтинг '))
my_list.append(new_rating)
l = len(my_list)
ind1 = l-2
ind2 = l-1
while ind1 >= 0:
    if my_list[ind1] < my_list[ind2]:
        my_list[ind1], my_list[ind2] = my_list[ind2], my_list[ind1]
        ind2 = ind1
    ind1 -= 1
print(my_list)


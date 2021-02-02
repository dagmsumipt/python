my_str = [word for word in input('Введите строку ').split(' ')]
def int_func(s):
    if s[0].isupper() == 0:
        return s[0].upper()+s[1:]
    else:
        return s
my_str1 = []
for word in my_str:
    my_str1.append(int_func(word))
print(' '.join(my_str1))
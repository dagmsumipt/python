from functools import reduce


def my_func(x, y):
    return x*y


print(reduce(my_func, range(100, 1001, 2)))


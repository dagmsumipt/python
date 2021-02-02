def my_func(x,y):
    z = 1
    for i in range(-y):
        z *= (1/x)
    return z
print(my_func(2,-3))

def sum_max_2(x, y, z):
    x1 = x+y
    x2 = y+z
    x3 = x+z
    return max(x1, x2, x3)
print(sum_max_2(1,2,3))
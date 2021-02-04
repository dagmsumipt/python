my_l = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
y = [my_l[i+1] for i in range(len(my_l)-1) if my_l[i+1] > my_l[i]]
print(y)

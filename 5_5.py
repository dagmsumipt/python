f = open('5_5.txt', 'w')
k = 0
while True:
    s = input()
    k += 1
    if s == ' ':
        break
    if k > 1:
        f.write(' '+s)
    else:
        f.write(s)
f.close()
f = open('5_5.txt', 'r')
print(sum([float(x) for x in f.readlines()[0].split(' ')]))

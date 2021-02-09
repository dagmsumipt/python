with open('5_3.txt', 'r', encoding = 'utf-8') as f:
    d = {}
    for line in f:
        l = line.split()
        d[l[0]] = float(l[1])
    for x, y in enumerate(d):
        if d[y] < 20000:
            print(y)
    print(sum(list(d.values()))/len(list(d.values())))
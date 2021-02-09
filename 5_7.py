import json
with open('5_7.txt', 'r', encoding='utf-8') as f:
    d = {}
    profit = []
    for line in f:
        l = line.split()
        d[l[0]] = float(l[2]) - float(l[3])
        if d[l[0]] > 0:
            profit.append(d[l[0]])
    d['average_profit'] = sum(profit)/len(profit)
with open('my_file.json', 'w', encoding='utf-8') as write_f:
    json.dump(d, write_f)

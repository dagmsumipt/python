f1 = open('5_4.txt', 'r', encoding = 'utf-8')
f2 = open('5_4_new.txt', 'w')
r = ['Один', 'Два', 'Три', 'Четыре']
for i, line in enumerate(f1.readlines()):
    line_new = r[i] + ' ' + ' '.join(line.split(' ')[1:])
    f2.write(line_new)
f1.close()
f2.close()

import re


def numbers_from_string(data):
    result = ' '.join(re.findall(r'\d+', data))
    return result


with open('5_6.txt', 'r', encoding='utf-8') as f:
    d = {}
    for line in f:
        li = line.split(' ')
        d[''.join(re.findall('[а-яА-ЯёЁ]', li[0]))] = sum([float(x) for x in numbers_from_string(line).split(' ')])
print(d)

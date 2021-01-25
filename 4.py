a = int(input('Введите число '))
x = a
max_digit = 0
while x > 0:
    digit = x % 10
    if digit > max_digit:
        max_digit = digit
    if max_digit == 9:
        break
    x = x//10
print(max_digit)
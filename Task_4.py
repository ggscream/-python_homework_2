# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input("Введите число в десятичной системе счисления: "))

if number == 0:
    print(0)
else:
    line = ""
    while number > 1:
        rest = str(number % 2)
        number = number // 2
        line += rest
    number = str(number)
    line += number
    print(int(''.join(reversed(line))))
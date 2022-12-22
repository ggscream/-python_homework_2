# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. ДОП

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def nega_fibonacci(n):

    if n == 0 or n == 1:
        return n
    elif n == -1:
        return -n
    elif n < 0:
        return int(nega_fibonacci(abs(n)) * (-1)**(n + 1))
    else:
        return nega_fibonacci(n - 1) + nega_fibonacci(n - 2)


n = int(input("Введите размер последовательности: "))
for i in range(-n, n + 1):
    print(nega_fibonacci(i), end=' ')
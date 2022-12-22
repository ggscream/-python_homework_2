# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

length = int(input("Определите длину списка: "))
numbers = []

for i in range(length):
    number = int(input(f"Введите любое целое число для {i + 1}-й позиции списка: "))
    numbers.append(number)

print(numbers)

sum = 0
for i in range(len(numbers)):
    if i % 2 == 1:
        sum += numbers[i]

print(sum)

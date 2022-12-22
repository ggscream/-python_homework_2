# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

length = int(input("Определите длину списка: "))
numbers = []

for i in range(length):
    number = float(input(f"Введите любое вещественное число для {i + 1}-й позиции списка: "))
    numbers.append(number)

print(numbers)

numbers_2 = []

for i in numbers:
    if i % 1 != 0:
        numbers_2.append(i % 1)

print(round(max(numbers_2) - min(numbers_2), 2))
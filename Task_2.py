# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

length = int(input("Определите длину списка: "))
numbers = []

for i in range(length):
    number = int(input(f"Введите любое целое число для {i + 1}-й позиции списка: "))
    numbers.append(number)

print(numbers)

results = []

if len(numbers) % 2 == 0:
    for i in range(int(len(numbers) / 2)):
        result = numbers[i] * numbers[-1 - i]
        results.append(result)
else:
    for i in range(int(len(numbers) / 2) + 1):
        result = numbers[i] * numbers[-1 - i]
        results.append(result)


print(results)
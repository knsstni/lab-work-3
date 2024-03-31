# Задание 1: Итерация и Циклы
print("Задание 1:")
for i in range(1, 21):
    print(i)
print()

# Задание 2: Работа с Списками и Циклами
print("Задание 2:")
numbers = list(range(1, 11))
for num in numbers:
    print(num ** 2)
print()

# Задание 3: Комбинирование Продуктов Питания
print("Задание 3:")
bread = ["white", "whole wheat"]
meat = ["turkey", "ham", "roast beef"]
vegetables = ["lettuce", "tomato", "onion"]
sauces = ["mayo", "mustard", "ketchup"]

for b in bread:
    for m in meat:
        for v in vegetables:
            for s in sauces:
                print(f"{b} + {m} + {v} + {s}")
print()

# Задание 4: Суммирование Чисел
print("Задание 4:")
sum_even = 0
sum_odd = 0

for i in range(1, 101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i

print("Сумма четных чисел:", sum_even)
print("Сумма нечетных чисел:", sum_odd)
print()

# Задание 5: Факториал Числа
print("Задание 5:")
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Введите число для вычисления факториала: "))
print("Факториал числа", num, "равен", factorial(num))
print()

# Задание 6: Обработка данных в личной базе данных
print("Задание 6:")
data = [
    {"имя": "Анна", "возраст": 25},
    {"имя": "Петр", "возраст": 30},
    {"имя": "Мария", "возраст": 35}
]

total_age = sum(person["возраст"] for person in data)
average_age = total_age / len(data)
print("Средний возраст:", average_age)
print()

# Задание 7: Индексирование и срезы списков
print("Задание 7:")
numbers = list(range(1, 11))
print(numbers[2:7])
print()

# Задание 8: Работа с операторами in/not in
print("Задание 8:")
fruits = ["яблоко", "груша", "апельсин"]

if "яблоко" in fruits:
    print("Список содержит яблоко.")
print()

# Задание 9: Использование кортежей для хранения данных
print("Задание 9:")
my_tuple = (42, "hello", [1, 2, 3])
print("Кортеж целиком:", my_tuple)
for item in my_tuple:
    print(item)
print()

# Задание 10: Методы работы со списками
print("Задание 10:")
numbers = list(range(1, 6))
numbers.append(6)
numbers.remove(3)
numbers.reverse()
print(numbers)

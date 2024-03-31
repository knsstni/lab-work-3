# Задание 1: Шифр Цезаря
def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# Пример использования:
text = "moon"  # ваше желаемое слово
shift = 3
encrypted_text = caesar_cipher(text, shift)
print("Зашифрованный текст:", encrypted_text)

# Задание 2: Работа с глобальными и локальными переменными
global_var = 100

def demo_function():
    local_var = 200
    print("Внутри функции:")
    print("Глобальная переменная global_var:", global_var)
    print("Локальная переменная local_var:", local_var)

demo_function()
print("Вне функции:")
print("Глобальная переменная global_var:", global_var)

# Задание 3: Использование параметров по умолчанию и ключевых параметров
def example_function(required_param, default_param=10):
    print("Обязательный параметр:", required_param)
    print("Параметр по умолчанию:", default_param)

example_function(10)
print("---")
example_function(10, 35)

# Задание 4: Возврат нескольких значений из функции
def min_max_avg(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

numbers_list = [500, 1, 666, 21, 25]
min_num, max_num, avg_num = min_max_avg(numbers_list)
print("Минимальное значение:", min_num)
print("Максимальное значение:", max_num)
print("Среднее значение:", avg_num)

# Задание 5: Форматирование строк
name = "Ангелина"
age = 21
formatted_string = "Привет, {}! Тебе {} год.".format(name, age)
print(formatted_string)
formatted_string = "Привет, {}! Тебе {} год.".format(name, age)
print(formatted_string)
formatted_string = "Привет, {name}! Тебе {age} год.".format(name=name, age=age)
print(formatted_string)






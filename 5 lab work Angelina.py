import json

# Задание 1: Создание и использование словаря
menu = {
    "Американо": 3000,
    "Капучино": 3500,
    "Латте": 4500,
    "Моккачино": 3600,
}

def get_price(drink):
    if drink in menu:
        print(f"Цена {drink}: {menu[drink]} KRW")
    else:
        print(f"Напитка {drink} нет в меню")

# Задание 2: Изменение и удаление элементов словаря
menu["Флэт Уайт"] = 3800
del menu["Американо"]

# Вывод итогового словаря
print("Итоговый словарь меню кафе после добавления напитка 'Флэт Уайт' и удаления 'Американо':")
for drink, price in menu.items():
    print(f"-{drink}: {price} KRW")
print()

# Задание 3: Работа с JSON
book_info = {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}
json_str = json.dumps(book_info)
print("Строка JSON, представляющая информацию о книге:", json_str)
parsed_book_info = json.loads(json_str)
print("Словарь, полученный из строки JSON:", parsed_book_info)
print()

# Задание 4: Использование методов словаря
print("Решение Задания 4:")
print("-Список ключей:", list(menu.keys()))
print("-Список значений:", list(menu.values()))
print("-Список пар ключ-значение:", list(menu.items()))
print()

# Задание 5: Словари и условные выражения
def drinks_below_price(menu, max_price):
    print(f"Напитки по цене ниже или равной {max_price} KRW:")
    for drink, price in menu.items():
        if price <= max_price:
            print(f"-{drink}: {price} KRW")

drinks_below_price(menu, 3600)

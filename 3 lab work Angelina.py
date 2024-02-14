import math

# Задание 1: Найти периметр квадрата
def find_perimeter_square(side_length):
    return 4 * side_length

# Задание 2: Найти площадь квадрата
def find_area_square(side_length):
    return side_length ** 2

# Задание 3: Найти площадь и периметр прямоугольника
def find_area_rectangle(a, b):
    area = a * b
    perimeter = 2 * (a + b)
    return area, perimeter

# Задание 4: Найти длину окружности
def find_circle_length(diameter):
    return math.pi * diameter

# Задание 5: Найти объем и площадь поверхности куба
def find_cube_volume_and_surface_area(side_length):
    volume = side_length ** 3
    surface_area = 6 * side_length ** 2
    return volume, surface_area

# Задание 6: Найти объем и площадь поверхности прямоугольного параллелепипеда
def find_parallelepiped_volume_and_surface_area(a, b, c):
    volume = a * b * c
    surface_area = 2 * (a * b + b * c + a * c)
    return volume, surface_area

# Задание 7: Найти длину окружности и площадь круга
def find_circle_length_and_area(radius):
    circle_length = 2 * math.pi * radius
    circle_area = math.pi * radius ** 2
    return circle_length, circle_area

# Задание 8: Найти среднее арифметическое двух чисел
def find_arithmetic_mean(a, b):
    return (a + b) / 2

# Задание 9: Найти среднее геометрическое двух чисел
def find_geometric_mean(a, b):
    return math.sqrt(a * b)

# Задание 10: Найти сумму, разность, произведение и частное квадратов двух чисел
def find_operations_on_squares(a, b):
    sum_squares = a ** 2 + b ** 2
    difference_squares = a ** 2 - b ** 2
    product_squares = a ** 2 * b ** 2
    if b != 0:
        quotient_squares = a ** 2 / b ** 2
    else:
        quotient_squares = "деление на ноль"
    return sum_squares, difference_squares, product_squares, quotient_squares

# Задание 11: Найти сумму, разность, произведение и частное модулей двух чисел
def find_operations_on_absolute_values(a, b):
    sum_abs = abs(a) + abs(b)
    difference_abs = abs(a) - abs(b)
    product_abs = abs(a) * abs(b)
    if abs(b) != 0:
        quotient_abs = abs(a) / abs(b)
    else:
        quotient_abs = "деление на ноль"
    return sum_abs, difference_abs, product_abs, quotient_abs

# Задание 12: Найти гипотенузу и периметр прямоугольного треугольника
def find_hypotenuse_and_perimeter(a, b):
    hypotenuse = math.sqrt(a ** 2 + b ** 2)
    perimeter = a + b + hypotenuse
    return hypotenuse, perimeter

# Задание 13: Найти площади кругов и кольца
def find_circle_areas(r1, r2):
    s1 = math.pi * r1 ** 2
    s2 = math.pi * r2 ** 2
    s3 = s1 - s2
    return s1, s2, s3

# Задание 14: Найти радиус и площадь круга по длине окружности
def find_circle_radius_and_area(length):
    radius = length / (2 * math.pi)
    area = math.pi * radius ** 2
    return radius, area

# Задание 15: Найти диаметр и длину окружности по площади круга
def find_circle_diameter_and_length(area):
    radius = math.sqrt(area / math.pi)
    diameter = 2 * radius
    length = 2 * math.pi * radius
    return diameter, length

# Задание 16: Найти расстояние между двумя точками на числовой оси
def find_distance_on_number_line(x1, x2):
    return abs(x2 - x1)

# Задание 17: Найти длины отрезков АС и ВС на числовой оси, а также их сумму
def find_segment_lengths(x_a, x_b, x_c):
    length_ac = abs(x_c - x_a)
    length_bc = abs(x_c - x_b)
    sum_lengths = length_ac + length_bc
    return length_ac, length_bc, sum_lengths

# Задание 18: Найти произведение длин отрезков АС и ВС на числовой оси
def find_product_of_segment_lengths(x_a, x_b, x_c):
    length_ac = abs(x_c - x_a)
    length_bc = abs(x_c - x_b)
    product_lengths = length_ac * length_bc
    return product_lengths

# Задание 19: Найти периметр и площадь прямоугольника по координатам вершин
def find_rectangle_perimeter_and_area(x1, y1, x2, y2):
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    perimeter = 2 * (width + height)
    area = width * height
    return perimeter, area

# Задание 20: Найти расстояние между двумя точками на плоскости
def find_distance_on_plane(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Ввод номера задания
task_number = int(input("Введите номер задания (от 1 до 20): "))

# Обработка ввода и вызов соответствующей функции в зависимости от номера задания
if task_number == 1:
    side_length = float(input("Введите длину стороны квадрата: "))
    perimeter = find_perimeter_square(side_length)
    print("Периметр квадрата равен:", perimeter)
elif task_number == 2:
    side_length = float(input("Введите длину стороны квадрата: "))
    area = find_area_square(side_length)
    print("Площадь квадрата равна:", area)
elif task_number == 3:
    a = float(input("Введите длину прямоугольника: "))
    b = float(input("Введите ширину прямоугольника: "))
    area, perimeter = find_area_rectangle(a, b)
    print("Площадь прямоугольника:", area)
    print("Периметр прямоугольника:", perimeter)
elif task_number == 4:
    diameter = float(input("Введите диаметр окружности: "))
    length = find_circle_length(diameter)
    print("Длина окружности равна:", length)
elif task_number == 5:
    side_length = float(input("Введите длину ребра куба: "))
    volume, surface_area = find_cube_volume_and_surface_area(side_length)
    print("Объем куба:", volume)
    print("Площадь поверхности куба:", surface_area)
elif task_number == 6:
    a = float(input("Введите длину прямоугольного параллелепипеда: "))
    b = float(input("Введите ширину прямоугольного параллелепипеда: "))
    c = float(input("Введите высоту прямоугольного параллелепипеда: "))
    volume, surface_area = find_parallelepiped_volume_and_surface_area(a, b, c)
    print("Объем параллелепипеда:", volume)
    print("Площадь поверхности параллелепипеда:", surface_area)
elif task_number == 7:
    radius = float(input("Введите радиус круга: "))
    length, area = find_circle_length_and_area(radius)
    print("Длина окружности:", length)
    print("Площадь круга:", area)
elif task_number == 8:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    arithmetic_mean = find_arithmetic_mean(a, b)
    print("Среднее арифметическое чисел:", arithmetic_mean)
elif task_number == 9:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    geometric_mean = find_geometric_mean(a, b)
    print("Среднее геометрическое чисел:", geometric_mean)
elif task_number == 10:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    sum_squares, difference_squares, product_squares, quotient_squares = find_operations_on_squares(a, b)
    print("Сумма квадратов чисел:", sum_squares)
    print("Разность квадратов чисел:", difference_squares)
    print("Произведение квадратов чисел:", product_squares)
    print("Частное квадратов чисел:", quotient_squares)
elif task_number == 11:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    sum_abs, difference_abs, product_abs, quotient_abs = find_operations_on_absolute_values(a, b)
    print("Сумма модулей чисел:", sum_abs)
    print("Разность модулей чисел:", difference_abs)
    print("Произведение модулей чисел:", product_abs)
    print("Частное модулей чисел:", quotient_abs)
elif task_number == 12:
    a = float(input("Введите длину первого катета: "))
    b = float(input("Введите длину второго катета: "))
    hypotenuse, perimeter = find_hypotenuse_and_perimeter(a, b)
    print("Гипотенуза треугольника:", hypotenuse)
    print("Периметр треугольника:", perimeter)
elif task_number == 13:
    r1 = float(input("Введите радиус первого круга: "))
    r2 = float(input("Введите радиус второго круга (меньше первого): "))
    s1, s2, s3 = find_circle_areas(r1, r2)
    print("Площадь первого круга:", s1)
    print("Площадь второго круга:", s2)
    print("Площадь кольца:", s3)
elif task_number == 14:
    length = float(input("Введите длину окружности: "))
    radius, area = find_circle_radius_and_area(length)
    print("Радиус окружности:", radius)
    print("Площадь круга:", area)
elif task_number == 15:
    area = float(input("Введите площадь круга: "))
    diameter, length = find_circle_diameter_and_length(area)
    radius, length = find_circle_diameter_and_length(area)
    print("Диаметр окружности:", diameter)
    print("Длина окружности:", length)
elif task_number == 16:
    x1 = float(input("Введите координату x первой точки: "))
    x2 = float(input("Введите координату x второй точки: "))
    distance = find_distance_on_number_line(x1, x2)
    print("Расстояние между точками на числовой оси:", distance)
elif task_number == 17:
    x_a = float(input("Введите координату x точки A: "))
    x_b = float(input("Введите координату x точки B: "))
    x_c = float(input("Введите координату x точки C: "))
    length_ac, length_bc, sum_lengths = find_segment_lengths(x_a, x_b, x_c)
    print("Длина отрезка AC:", length_ac)
    print("Длина отрезка BC:", length_bc)
    print("Сумма длин отрезков AC и BC:", sum_lengths)
elif task_number == 18:
    x_a = float(input("Введите координату x точки A: "))
    x_b = float(input("Введите координату x точки B: "))
    x_c = float(input("Введите координату x точки C: "))
    product_lengths = find_product_of_segment_lengths(x_a, x_b, x_c)
    print("Произведение длин отрезков AC и BC:", product_lengths)
elif task_number == 19:
    x1 = float(input("Введите координату x первой точки: "))
    y1 = float(input("Введите координату y первой точки: "))
    x2 = float(input("Введите координату x второй точки: "))
    y2 = float(input("Введите координату y второй точки: "))
    perimeter, area = find_rectangle_perimeter_and_area(x1, y1, x2, y2)
    print("Периметр прямоугольника:", perimeter)
    print("Площадь прямоугольника:", area)
elif task_number == 20:
    x1 = float(input("Введите координату x первой точки: "))
    y1 = float(input("Введите координату y первой точки: "))
    x2 = float(input("Введите координату x второй точки: "))
    y2 = float(input("Введите координату y второй точки: "))
    distance = find_distance_on_plane(x1, y1, x2, y2)
    print("Расстояние между точками на плоскости:", distance)
else:
    print("Неверный номер задания. Пожалуйста, выберите число от 1 до 20.")

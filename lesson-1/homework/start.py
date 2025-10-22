Вопросы:
Given a side of square. Find its perimeter and area.
Given diameter of circle. Find its length.
Given two numbers a and b. Find their mean.
Given two numbers a and b. Find their sum, product and square of each number.

Ответы :

# 1. Квадрат
s = float(input("Введите сторону квадрата: "))
perimeter_square = 4 * s
area_square = s ** 2
print(f"Периметр квадрата = {perimeter_square}")
print(f"Площадь квадрата = {area_square}")

# 2. Окружность
d = float(input("\nВведите диаметр окружности: "))
circumference = math.pi * d
print(f"Длина окружности = {circumference}")

# 3. Среднее двух чисел
a = float(input("\nВведите число a: "))
b = float(input("Введите число b: "))
mean_ab = (a + b) / 2
print(f"Среднее арифметическое чисел a и b = {mean_ab}")

# 4. Сумма, произведение и квадраты
sum_ab = a + b
prod_ab = a * b
square_a = a ** 2
square_b = b ** 2
print(f"Сумма = {sum_ab}")
print(f"Произведение = {prod_ab}")
print(f"Квадрат a = {square_a}")
print(f"Квадрат b = {square_b}")

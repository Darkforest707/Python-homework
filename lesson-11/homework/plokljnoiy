Создание виртуальной среды и установка пакетов
# Создание виртуальной среды
python -m venv myenv

# Активация виртуальной среды (Windows)
myenv\Scripts\activate

# Активация виртуальной среды (Mac/Linux)
source myenv/bin/activate

# Установка пакетов (пример)
pip install requests numpy pandas

2 Создание пользовательских модулей
math_operations.py
# math_operations.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

string_utils.py
# string_utils.py

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

3 Создание пакетов
Пакет geometry
geometry/
    __init__.py
    circle.py

circle.py
# geometry/circle.py
import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius

Пакет file_operations
file_operations/
    __init__.py
    file_reader.py
    file_writer.py

file_reader.py
# file_operations/file_reader.py

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

file_writer.py
# file_operations/file_writer.py

def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

Пример использования модулей и пакетов
# main.py

# Используем math_operations
import math_operations as mo
print(mo.add(10, 5))
print(mo.divide(10, 2))

# Используем string_utils
import string_utils as su
print(su.reverse_string("hello"))
print(su.count_vowels("hello world"))

# Используем пакет geometry
from geometry.circle import calculate_area, calculate_circumference
print(calculate_area(5))
print(calculate_circumference(5))

# Используем пакет file_operations
from file_operations.file_writer import write_file
from file_operations.file_reader import read_file

write_file("example.txt", "Hello Python!")
print(read_file("example.txt"))

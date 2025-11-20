Homework 1
import pandas as pd
import numpy as np

# Данные
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# 1️ Переименование колонок
df.rename(columns={'First Name': 'first_name', 'Age': 'age'}, inplace=True)

# 2️ Печать первых 3 строк
print("First 3 rows:\n", df.head(3))

# 3️ Средний возраст
mean_age = df['age'].mean()
print("\nMean age:", mean_age)

# 4️ Выбор только колонок 'first_name' и 'City'
print("\nName and City columns:\n", df[['first_name', 'City']])

# 5️ Добавление новой колонки 'Salary' с случайными значениями
np.random.seed(42)  # для воспроизводимости
df['Salary'] = np.random.randint(3000, 7000, size=len(df))

# 6️ Печать DataFrame и статистики
print("\nDataFrame with Salary:\n", df)
print("\nSummary statistics:\n", df.describe())

Homework 2
# Данные по продажам и расходам
sales_data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}

sales_and_expenses = pd.DataFrame(sales_data)

# Максимум
print("Max Sales:", sales_and_expenses['Sales'].max())
print("Max Expenses:", sales_and_expenses['Expenses'].max())

# Минимум
print("Min Sales:", sales_and_expenses['Sales'].min())
print("Min Expenses:", sales_and_expenses['Expenses'].min())

# Среднее
print("Average Sales:", sales_and_expenses['Sales'].mean())
print("Average Expenses:", sales_and_expenses['Expenses'].mean())

Homework 3
# Данные по расходам
expenses_data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

expenses = pd.DataFrame(expenses_data)

# Используем Category как индекс
expenses.set_index('Category', inplace=True)

# Максимальные расходы по категориям
print("Max expense per category:\n", expenses.max(axis=1))

# Минимальные расходы по категориям
print("\nMin expense per category:\n", expenses.min(axis=1))

# Средние расходы по категориям
print("\nAverage expense per category:\n", expenses.mean(axis=1))

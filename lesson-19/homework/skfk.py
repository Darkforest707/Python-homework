Homework Assignment 1: Analyzing Sales Data
import pandas as pd

# Загрузка данных
sales_df = pd.read_csv("task\\sales_data.csv")

# 1️ Группировка по категории
category_stats = sales_df.groupby('Category').agg(
    total_quantity=('Quantity', 'sum'),
    avg_price=('Price', 'mean'),
    max_quantity=('Quantity', 'max')
).reset_index()
print("Category statistics:\n", category_stats)

# 2️ Топ-продукт по каждой категории
top_products = sales_df.groupby(['Category', 'Product']).agg(total_quantity=('Quantity', 'sum'))
top_products = top_products.reset_index()
top_products = top_products.loc[top_products.groupby('Category')['total_quantity'].idxmax()]
print("\nTop-selling products by category:\n", top_products)

# 3️ Дата с наибольшей суммой продаж
sales_df['TotalSale'] = sales_df['Quantity'] * sales_df['Price']
top_sale_date = sales_df.groupby('Date')['TotalSale'].sum().idxmax()
print("\nDate with highest total sales:", top_sale_date)

Homework Assignment 2: Examining Customer Orders
# Загрузка данных
orders_df = pd.read_csv("task\\customer_orders.csv")

# 1️ Группировка по CustomerID и фильтрация клиентов с >= 20 заказов
customer_order_counts = orders_df.groupby('CustomerID').size()
customers_20plus = customer_order_counts[customer_order_counts >= 20].index
filtered_customers = orders_df[orders_df['CustomerID'].isin(customers_20plus)]
print("Customers with at least 20 orders:\n", filtered_customers['CustomerID'].unique())

# 2️ Клиенты, заказывавшие товары со средней ценой > $120
customer_avg_price = orders_df.groupby('CustomerID')['Price'].mean()
high_avg_price_customers = customer_avg_price[customer_avg_price > 120].index
print("\nCustomers with avg price per unit > $120:\n", high_avg_price_customers)

# 3️ Общая сумма и количество по каждому продукту, фильтр по количеству >=5
product_totals = orders_df.groupby('Product').agg(
    total_quantity=('Quantity', 'sum'),
    total_price=('Price', lambda x: (x*orders_df.loc[x.index, 'Quantity']).sum())
)
product_totals_filtered = product_totals[product_totals['total_quantity'] >= 5]
print("\nProducts with total quantity >= 5:\n", product_totals_filtered)

Homework Assignment 3: Population Salary Analysis
import sqlite3
import pandas as pd

# Подключение к базе данных
conn = sqlite3.connect("task\\population.db")
population_df = pd.read_sql("SELECT * FROM population", conn)
conn.close()

# Загрузка Salary Band категорий
salary_band_df = pd.read_excel("task\\population salary analysis.xlsx")

# Объединение данных с категориями
population_df = population_df.merge(salary_band_df, on='Salary', how='left')

# 1️ % населения по Salary Band
salary_counts = population_df['SalaryBand'].value_counts()
salary_percentage = 100 * salary_counts / len(population_df)
print("Percentage of population by salary band:\n", salary_percentage)

# 2️ Средняя зарплата по Salary Band
avg_salary_band = population_df.groupby('SalaryBand')['Salary'].mean()
print("\nAverage salary by salary band:\n", avg_salary_band)

# 3️ Медианная зарплата по Salary Band
median_salary_band = population_df.groupby('SalaryBand')['Salary'].median()
print("\nMedian salary by salary band:\n", median_salary_band)

# 4️ Количество населения в каждой категории
count_salary_band = population_df['SalaryBand'].value_counts()
print("\nNumber of population in each salary band:\n", count_salary_band)

# 5️ Аналогичные расчёты по каждому штату
state_stats = population_df.groupby(['State', 'SalaryBand']).agg(
    population_count=('Salary', 'count'),
    avg_salary=('Salary', 'mean'),
    median_salary=('Salary', 'median')
).reset_index()
print("\nState-wise salary statistics:\n", state_stats)

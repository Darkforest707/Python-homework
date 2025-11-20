import sqlite3
import pandas as pd

# Подключение к базе данных
conn = sqlite3.connect("task\\chinook.db")

# Загрузка таблиц
customers = pd.read_sql("SELECT CustomerId, FirstName, LastName FROM Customer", conn)
invoices = pd.read_sql("SELECT InvoiceId, CustomerId FROM Invoice", conn)
invoice_items = pd.read_sql("SELECT InvoiceId, UnitPrice, Quantity, TrackId FROM InvoiceLine", conn)
tracks = pd.read_sql("SELECT TrackId, AlbumId FROM Track", conn)
albums = pd.read_sql("SELECT AlbumId, Title FROM Album", conn)

conn.close()

# ===============================
# 1️ Customer Purchases Analysis
# ===============================

# Сумма покупки по каждой позиции
invoice_items['Total'] = invoice_items['UnitPrice'] * invoice_items['Quantity']

# Сумма покупок по каждому Invoice
invoice_totals = invoice_items.groupby('InvoiceId')['Total'].sum().reset_index()

# Сумма покупок по каждому Customer
invoice_totals = invoice_totals.merge(invoices[['InvoiceId','CustomerId']], on='InvoiceId')
customer_totals = invoice_totals.groupby('CustomerId')['Total'].sum().reset_index()

# Добавляем имя клиента
customer_totals = customer_totals.merge(customers, on='CustomerId')
customer_totals['FullName'] = customer_totals['FirstName'] + ' ' + customer_totals['LastName']

# Топ-5 клиентов по сумме покупок
top5_customers = customer_totals.sort_values(by='Total', ascending=False).head(5)
print("Top 5 customers by total purchase amount:\n")
print(top5_customers[['CustomerId','FullName','Total']])

# =========================================
# 2️ Album vs Individual Track Purchases
# =========================================

# Сколько треков в каждом альбоме
album_tracks_count = tracks.groupby('AlbumId')['TrackId'].count().reset_index()
album_tracks_count.rename(columns={'TrackId':'TotalTracksInAlbum'}, inplace=True)

# Объединяем InvoiceLine с треками для получения AlbumId
invoice_items_album = invoice_items.merge(tracks[['TrackId','AlbumId']], on='TrackId')

# Считаем сколько треков каждой покупки было куплено для каждого альбома и клиента
album_purchase_counts = invoice_items_album.groupby(['CustomerId','AlbumId'])['TrackId'].count().reset_index()
album_purchase_counts = album_purchase_counts.merge(album_tracks_count, on='AlbumId')

# Проверяем, куплен ли весь альбом
album_purchase_counts['FullAlbumPurchased'] = album_purchase_counts['TrackId'] == album_purchase_counts['TotalTracksInAlbum']

# Для каждого клиента считаем, есть ли хотя бы один альбом куплен полностью
customer_album_pref = album_purchase_counts.groupby('CustomerId')['FullAlbumPurchased'].all().reset_index()
customer_album_pref['Preference'] = customer_album_pref['FullAlbumPurchased'].apply(lambda x: 'Full Album' if x else 'Individual Tracks')

# Рассчитываем процент клиентов по предпочтениям
preference_summary = customer_album_pref['Preference'].value_counts(normalize=True)*100
print("\nPercentage of customers preferring full albums vs individual tracks:\n")
print(preference_summary)

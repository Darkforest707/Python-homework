import sqlite3

# 1️ Создание базы данных и таблицы Roster
conn = sqlite3.connect("starfleet.db")  # Создает файл базы данных
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# 2️ Вставка данных
# Сначала очищаем таблицу, чтобы не дублировать при повторном запуске
cursor.execute("DELETE FROM Roster")

roster_data = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]

cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", roster_data)
conn.commit()

# 3️ Обновление имени Jadzia Dax на Ezri Dax
cursor.execute("UPDATE Roster SET Name = ? WHERE Name = ?", ("Ezri Dax", "Jadzia Dax"))
conn.commit()

# 4️ Выборка всех Bajoran с их именами и возрастом
cursor.execute("SELECT Name, Age FROM Roster WHERE Species = ?", ("Bajoran",))
bajorans = cursor.fetchall()

print("Bajoran crew members:")
for name, age in bajorans:
    print(f"Name: {name}, Age: {age}")

# Закрытие соединения
conn.close()

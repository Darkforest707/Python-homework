1️ JSON Parsing – students.json

Пример students.json:

[
    {"name": "Alice", "age": 20, "major": "Math"},
    {"name": "Bob", "age": 22, "major": "Physics"},
    {"name": "Charlie", "age": 19, "major": "Computer Science"}
]


Python скрипт для чтения и вывода:

import json

with open("students.json", "r", encoding="utf-8") as f:
    students = json.load(f)

for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Major: {student['major']}")

2 Weather API – OpenWeatherMap

Для этого нужно зарегистрироваться и получить API key: https://openweathermap.org/api

import requests

city = "Tashkent"
api_key = "YOUR_API_KEY"  # вставь сюда свой API ключ
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Weather: {data['weather'][0]['description']}")
else:
    print("Error fetching weather data:", data.get("message"))

3 JSON Modification – books.json

Пример books.json:

[
    {"title": "Book A", "author": "Author 1", "year": 2020},
    {"title": "Book B", "author": "Author 2", "year": 2019}
]


Python скрипт:

import json

file_path = "books.json"

def load_books():
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_books(books):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(books, f, indent=4)

books = load_books()

# Добавление книги
new_book = {"title": "Book C", "author": "Author 3", "year": 2021}
books.append(new_book)

# Обновление книги
for book in books:
    if book["title"] == "Book A":
        book["year"] = 2021

# Удаление книги
books = [book for book in books if book["title"] != "Book B"]

save_books(books)
print("Updated books:", books)

4 Movie Recommendation System – OMDB API

Для этого нужно зарегистрироваться и получить API key: http://www.omdbapi.com/apikey.aspx

import requests
import random

api_key = "YOUR_API_KEY"  # вставь сюда свой API ключ
genre = input("Enter movie genre: ").lower()

url = f"http://www.omdbapi.com/?apikey={api_key}&type=movie&s={genre}"

response = requests.get(url)
data = response.json()

if data.get("Response") == "True":
    movies = data.get("Search", [])
    if movies:
        movie = random.choice(movies)
        print("Movie Recommendation:")
        print(f"Title: {movie['Title']}")
        print(f"Year: {movie['Year']}")
        print(f"IMDB ID: {movie['imdbID']}")
    else:
        print("No movies found in this genre.")
else:
    print("Error:", data.get("Error"))

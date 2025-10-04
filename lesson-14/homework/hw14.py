# Task: JSON Parsing
#######33 write a Python script that reads the students.jon JSON file and prints details of each student.


import json  # JSON bilan ishlash uchun

# JSON faylni ochish
with open("students.json", "r") as file:
    data = json.load(file)  # fayldan JSON ma’lumotni o‘qish

# Har bir talabani chiqarish
for student in data["students"]:
    print(f"👤 Name: {student['name']}")
    print(f"🎓 Age: {student['age']}")
    print(f"🏫 Grade: {student['grade']}")
    print("-" * 30)


#################2. Task: Weather API
# Use this url : https://openweathermap.org/


import requests

# OpenWeatherMap API kalitingiz (saytdan olasiz)
API_KEY = "YOUR_API_KEY_HERE"

# Shahar nomi (masalan, Tashkent)
city = "Tashkent"

# API manzili (metric = harorat Selsiy bo‘lishi uchun)
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# API ga so‘rov yuborish
response = requests.get(url)

# Natijani JSON formatda olish
data = response.json()

# Agar so‘rov muvaffaqiyatli bo‘lsa
if response.status_code == 200:
    print(f"🌆 City: {data['name']}")
    print(f"🌡️ Temperature: {data['main']['temp']} °C")
    print(f"💧 Humidity: {data['main']['humidity']} %")
    print(f"💨 Wind Speed: {data['wind']['speed']} m/s")
    print(f"☁️ Weather: {data['weather'][0]['description'].title()}")
else:
    print("❌ Error:", data.get("message", "Could not fetch weather data"))


# 3. Task: JSON Modification
# Write a program that allows users to add new books, 
# update existing book information, and delete books from the books.json JSON file.

import json
import os

# JSON fayl nomi
FILE_NAME = "books.json"

# Fayl mavjud bo‘lmasa, bo‘sh ro‘yxat yaratamiz
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        json.dump([], f, indent=4)

# 📖 JSON fayldan ma’lumotni o‘qish
def read_books():
    with open(FILE_NAME, "r") as f:
        return json.load(f)

# 💾 JSON faylga ma’lumot yozish
def write_books(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

# ➕ Yangi kitob qo‘shish
def add_book():
    books = read_books()
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter publication year: ")

    new_book = {"title": title, "author": author, "year": year}
    books.append(new_book)
    write_books(books)
    print(f"✅ Book '{title}' added successfully!")

# 🔁 Kitob ma’lumotini yangilash
def update_book():
    books = read_books()
    title = input("Enter the title of the book to update: ")

    for book in books:
        if book["title"].lower() == title.lower():
            book["author"] = input("Enter new author name: ")
            book["year"] = input("Enter new publication year: ")
            write_books(books)
            print("✅ Book updated successfully!")
            return
    print("❌ Book not found!")

# ❌ Kitobni o‘chirish
def delete_book():
    books = read_books()
    title = input("Enter the title of the book to delete: ")

    updated_books = [b for b in books if b["title"].lower() != title.lower()]()_




# 4. Task: Movie Recommendation System
# Use this url http://www.omdbapi.com/ to fetch information about movies.
# Create a program that asks users for a movie genre and recommends a random movie from that genre.

import requests
import random

# OMDb API dan foydalanish uchun API kalit kerak bo‘ladi (https://www.omdbapi.com/apikey.aspx saytidan oling)
API_KEY = "YOUR_API_KEY"  # <-- bu yerga o'z API kalitingni yoz

def get_movies_by_genre(genre):
    """Berilgan janr bo‘yicha filmlar ro‘yxatini qaytaradi."""
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={genre}&type=movie"
    response = requests.get(url)
    data = response.json()

    if data.get("Response") == "True":
        return data["Search"]
    else:
        print("Hech qanday film topilmadi.")
        return []

def recommend_movie(genre):
    """Tasodifiy filmni tavsiya qiladi."""
    movies = get_movies_by_genre(genre)
    if movies:
        movie = random.choice(movies)
        print(f"\n🎥 Tavsiya etilgan film: {movie['Title']}")
        print(f"📅 Yili: {movie['Year']}")
        print(f"🔗 IMDB sahifasi: https://www.imdb.com/title/{movie['imdbID']}/")

# --- Dastur ishga tushadi ---
user_genre = input("Film janrini kiriting (masalan: Action, Comedy, Drama): ")
recommend_movie(user_genre)




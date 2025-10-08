
# 1. Create a new database with a table named Roster that has three fields: Name, Species, and Age. 
# The Name and Species columns should be text fields, and the Age column should be an integer field.

import sqlite3

# 1️⃣ Yangi (yoki mavjud) ma’lumotlar bazasiga ulanamiz
conn = sqlite3.connect("my_database.db")

# 2️⃣ Cursor obyektini yaratamiz — bu orqali SQL buyruqlarni bajarish mumkin
cursor = conn.cursor()

# 3️⃣ Jadval (table) yaratamiz
cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# 4️⃣ O‘zgarishlarni saqlaymiz
conn.commit()

# 5️⃣ Ulanishni yopamiz
conn.close()

print("✅ Database va Roster jadvali muvaffaqiyatli yaratildi!")

2. # Populate your new table with the following values:


import sqlite3

# Ma'lumotlar bazasiga ulanamiz
conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

# Kiritiladigan ma'lumotlar
roster_data = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]

# Ma'lumotlarni jadvalga kiritish
cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", roster_data)

# O'zgarishlarni saqlash
conn.commit()

# Natijani tekshirish uchun jadvaldagi ma'lumotlarni chiqaramiz
cursor.execute("SELECT * FROM Roster")
rows = cursor.fetchall()

print("✅ Jadvalga quyidagi ma'lumotlar qo'shildi:\n")
for row in rows:
    print(row)

# Ulanishni yopamiz
conn.close()

# 3. Update the Name of Jadzia Dax to be Ezri Dax

import sqlite3

# Ma'lumotlar bazasiga ulanamiz
conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

# Jadzia Dax nomini Ezri Dax ga o'zgartiramiz
cursor.execute("""
    UPDATE Roster
    SET Name = 'Ezri Dax'
    WHERE Name = 'Jadzia Dax'
""")

# O'zgarishlarni saqlaymiz
conn.commit()

# Yangilangan natijani ko'rish
cursor.execute("SELECT * FROM Roster")
rows = cursor.fetchall()

print("✅ Jadval yangilandi:\n")
for row in rows:
    print(row)

# Ulanishni yopamiz
conn.close()


# 4. Display the Name and Age of everyone in the table classified as Bajoran.

import sqlite3

# Ma'lumotlar bazasiga ulanamiz
conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

# Faqat Bajoran turidagilarni chiqaramiz
cursor.execute("""
    SELECT Name, Age
    FROM Roster
    WHERE Species = 'Bajoran'
""")

# Natijalarni olish
rows = cursor.fetchall()

print("🧍‍♂️ Bajoran turlarining ismi va yoshi:\n")
for row in rows:
    print(f"Name: {row[0]}, Age: {row[1]}")

# Ulanishni yopamiz
conn.close()

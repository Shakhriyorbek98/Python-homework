# Lesson_13 homeworks 

######################## 1. Age Calculator: Ask the user to enter their birthdate. 
# Calculate and print their age in years, months, and days.

from datetime import date

birth_year=int(input("Tug'ilgan yil:"))
birth_month=int(input("Tug'ilgan oy:"))
birth_day=int(input("Tug'ilgan kun:"))

birth_date=date(birth_year, birth_month, birth_day)
today=date.today()

years=today.year-birth_date.year
months=today.month-birth_date.month
days=today.day-birth_date.day

if days<0:
    months-=1

    previous_month = (today.month - 1) or 12
    previous_year = today.year if today.month > 1 else today.year - 1
    days_in_prev_month = (date(previous_year, previous_month % 12 + 1, 1) - date(previous_year, previous_month, 1)).days
    days += days_in_prev_month

if months < 0:
    years -= 1
    months += 12

print(f'Sizning yoshingiz:{years} yil, {months} oy, {days} kun.')


#################################3 2. Days Until Next Birthday: Similar to the first exercise, 
# but this time, calculate and print the number of days remaining until the user's next birthday.


from datetime import date

# Foydalanuvchidan tug‘ilgan sanasini so‘raymiz
birth_year = int(input("Tug‘ilgan yilingizni kiriting (masalan, 2000): "))
birth_month = int(input("Tug‘ilgan oyingizni kiriting (1-12): "))
birth_day = int(input("Tug‘ilgan kuningizni kiriting (1-31): "))

today = date.today()
current_year = today.year

# Shu yilgi tug‘ilgan kun sanasini yaratamiz
next_birthday = date(current_year, birth_month, birth_day)

# Agar tug‘ilgan kuni bu yil o‘tib ketgan bo‘lsa — keyingi yilni olamiz
if next_birthday < today:
    next_birthday = date(current_year + 1, birth_month, birth_day)

# Tug‘ilgan kungacha qolgan kunlar soni
days_remaining = (next_birthday - today).days

print(f"Sizning keyingi tug‘ilgan kuningizgacha {days_remaining} kun qoldi! 🎉")


############### 3. Meeting Scheduler: Ask the user to enter the current date and time, 
# as well as the duration of a meeting in hours and minutes. 
# Calculate and print the date and time when the meeting will end.

from datetime import datetime, timedelta

# Foydalanuvchidan hozirgi sana va vaqtni kiritishni so‘raymiz
current_date_str = input("Joriy sana va vaqtni kiriting (masalan, 2025-10-04 14:30): ")

# Matndan datetime obyektiga o‘tkazamiz
current_date = datetime.strptime(current_date_str, "%Y-%m-%d %H:%M")

# Uchrashuv davomiyligini so‘raymiz
hours = int(input("Uchrashuv necha soat davom etadi? "))
minutes = int(input("Qo‘shimcha necha daqiqa davom etadi? "))

# Uchrashuv tugash vaqtini hisoblaymiz
meeting_duration = timedelta(hours=hours, minutes=minutes)
end_time = current_date + meeting_duration

print(f"\nUchrashuv tugaydigan vaqt: {end_time.strftime('%Y-%m-%d %H:%M')}")


##################### 4. Timezone Converter: Create a program that allows the user to enter a date and 
# time along with their current timezone, # and then convert and print the date and time in another timezone of their choice. 

from datetime import datetime
import pytz

# Foydalanuvchidan ma'lumotlarni olish
date_str = input("Sana va vaqtni kiriting (masalan: 2025-10-04 14:30): ")
current_tz_str = input("Hozirgi vaqt zonasini kiriting (masalan: Asia/Tashkent): ")
target_tz_str = input("O‘zgartiriladigan vaqt zonasini kiriting (masalan: America/New_York): ")

# Foydalanuvchi kiritgan sanani datetime obyektiga o‘tkazamiz
naive_datetime = datetime.strptime(date_str, "%Y-%m-%d %H:%M")

# Vaqt zonalarini o‘rnatamiz
current_tz = pytz.timezone(current_tz_str)
target_tz = pytz.timezone(target_tz_str)

# Sana va vaqtni joriy zonaga mahkamlab, keyin boshqa zonaga o‘tkazamiz
localized_datetime = current_tz.localize(naive_datetime)
converted_datetime = localized_datetime.astimezone(target_tz)

# Natijani chiqaramiz
print(f"\n{current_tz_str} zonasidagi vaqt: {localized_datetime.strftime('%Y-%m-%d %H:%M')}")
print(f"{target_tz_str} zonasidagi mos vaqt: {converted_datetime.strftime('%Y-%m-%d %H:%M')}")


########## 5.  Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, 
# and then continuously print the time remaining until that point in regular intervals (e.g., every second).

from datetime import datetime
import time

# Foydalanuvchidan kelajakdagi sana va vaqtni olish
future_str = input("Kelajakdagi sana va vaqtni kiriting (masalan: 2025-10-05 18:30): ")

# Stringni datetime obyektiga aylantirish
future_time = datetime.strptime(future_str, "%Y-%m-%d %H:%M")

print("\nTaymer boshlandi!\n")

# Cheksiz sikl (loop) orqali vaqtni kuzatamiz
while True:
    current_time = datetime.now()
    remaining = future_time - current_time

    if remaining.total_seconds() <= 0:
        print("⏰ Time’s up!")
        break

    # Qolgan vaqtni soat, daqiqa, soniya tarzida ajratamiz
    days = remaining.days
    hours, remainder = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"Qolgan vaqt: {days} kun, {hours:02d}:{minutes:02d}:{seconds:02d}", end="\r")

    time.sleep(1)  # Har 1 soniyada yangilab turadi



# 6. Email Validator: Write a program that validates email addresses. 
# Ask the user to input an email address, and check if it follows a valid email format.

import re

# Foydalanuvchidan email manzilni olish
email = input("Email manzilingizni kiriting: ")

# Emailni tekshirish uchun oddiy regex namunasi
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Moslikni tekshirish
if re.match(pattern, email):
    print("✅ Email manzili to‘g‘ri formatda!")
else:
    print("❌ Email manzili noto‘g‘ri formatda!")

# 7. Phone Number Formatter: Create a program that takes a phone number as input and 
# formats it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".

def format_phone_number(phone):
    # Faqat raqamlarni ajratib olish
    digits = ''.join(filter(str.isdigit, phone))

    # Tekshirish — agar uzunligi 10 ta bo‘lmasa, noto‘g‘ri deb chiqarish
    if len(digits) != 10:
        return "❌ Noto‘g‘ri raqam! 10 ta raqam kiritilishi kerak."

    # Formatlash: (123) 456-7890
    formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    return formatted


# Foydalanuvchidan raqam olish
user_input = input("Telefon raqamingizni kiriting (faqat raqamlar): ")
print("📞 Formatlangan raqam:", format_phone_number(user_input))


# 8. Password Strength Checker: Implement a password strength checker. Ask the user to input a password and 
# check if it meets certain criteria # (e.g., minimum length, contains at least one uppercase letter, 
# one lowercase letter, and one digit).

import re  # regex kutubxona

def check_password_strength(password):
    # 1. Eng kam uzunlik 8 ta belgi
    if len(password) < 8:
        return "❌ Parol juda qisqa! Eng kamida 8 ta belgi bo‘lishi kerak."

    # 2. Katta harf borligini tekshirish
    if not re.search(r"[A-Z]", password):
        return "❌ Parolda kamida bitta katta harf (A–Z) bo‘lishi kerak."

    # 3. Kichik harf borligini tekshirish
    if not re.search(r"[a-z]", password):
        return "❌ Parolda kamida bitta kichik harf (a–z) bo‘lishi kerak."

    # 4. Raqam borligini tekshirish
    if not re.search(r"\d", password):
        return "❌ Parolda kamida bitta raqam (0–9) bo‘lishi kerak."

    # 5. Maxsus belgi borligini tekshirish
    if not re.search(r"[@$!%*?&]", password):
        return "❌ Parolda kamida bitta maxsus belgi (@, $, !, %, *, ?, &) bo‘lishi kerak."

    # Hammasi joyida bo‘lsa
    return "✅ Parol kuchli! 👏"


# Foydalanuvchidan parol olish
password = input("Parolni kiriting: ")
print(check_password_strength(password))


####### 9. Word Finder: Develop a program that finds all occurrences of a specific word in a given text. 
# Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.

import re  # regex kutubxona

# Namunaviy matn
text = """Python is an amazing programming language.
Python is used for data science, web development, and automation.
Many developers love Python because it is simple and powerful."""

# Foydalanuvchidan so‘z kiritish
word = input("Qaysi so‘zni qidirmoqchisiz? ")

# Regex orqali barcha mosliklarni topish (katta-kichik farq qilmasdan)
matches = re.findall(word, text, re.IGNORECASE)

# Natija chiqarish
if matches:
    print(f"🔍 '{word}' so‘zi matnda {len(matches)} marta uchradi.")
else:
    print(f"❌ '{word}' so‘zi matnda topilmadi.")






# ###############10. Date Extractor: Write a program that extracts dates from a given text. 
# Ask the user to input a text, and then identify and print all the dates present in the text.

import re  # regex kutubxona

# Foydalanuvchidan matn kiritish
text = input("Matn kiriting (unda sanalar bo‘lsin, masalan: 12/05/2024 yoki 2025-10-04):\n")

# Sanalarni topish uchun regex shabloni
pattern = r"\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b"  # Masalan: 12/05/2024 yoki 3-7-23
pattern_alt = r"\b\d{4}[-/]\d{1,2}[-/]\d{1,2}\b"  # Masalan: 2025-10-04 formatiga

# Barcha mosliklarni topish
dates = re.findall(pattern, text) + re.findall(pattern_alt, text)

# Natija chiqarish
if dates:
    print("📅 Topilgan sanalar:")
    for d in dates:
        print("-", d)
else:
    print("❌ Matnda hech qanday sana topilmadi.")

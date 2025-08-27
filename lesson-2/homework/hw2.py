# 1. Age Calculator

name=input("Ismingizni kiriting:")
year_of_birth=int(input("Tug'ilgan yilingizni kiriting:"))

import datetime
current_year= datetime.datetime.now().year

age = current_year-year_of_birth

print("Ismingizni kiriting:", name)
print("Tug'ilgan yilingizni kiriting:", year_of_birth)
print("Yoshingizni kiriting:", age)


# 2. Extract car names from the following text:
txt = 'LMaasleitbtui'

print(txt[::2]) 
print(txt[1::2])


# 3. Extract car names from the following text:

txt = 'MsaatmiazD'
txt[::2]

reverse_txt=txt[::-1]
print( reverse_txt)
reverse_txt[0::2]

# 4. Extract the residence area from the following text:

txt = "I'am John. I am from London"
txt = "I'am John. I am from London"
my_string=txt
my_string.split()[5]

# 5. Write a Python program that takes a user input string and prints it in reverse order.

name=input("input_string")
reverse_name=name[::-1]
print

# 6. Write a Python program that counts the number of vowels in a given string.



text=input("Given_string")
text
vowels="aeiouAEIOU"
count=0
for ch in text:
    if ch in vowels:
        count+=1

print("number of vowels:", count)

# 7. Write a Python program that takes a list of numbers as input and prints the maximum value.

numbers=input("Raqamlar:")
numbers =[float(x) for x in numbers.split(",")]
max_value=max(numbers)
print("Eng katta qiymat:", max_value)

# 8. Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).

word=input("So'z kiritiladi:")
reversed_word=word[::-1]

if word==reversed_word:
    print("Bu so'z palindrome!")
else:
    print("Bu so'z palindrome emas!")

# 9. Write a Python program that extracts and prints the domain from an email address provided by the user.

email = input("Email manzilingizni kiriting: ")

domain = email.split("@")[1]

print("Email domeni:", domain)

# 10. Write a Python program to generate a random password containing letters, digits, and special characters.

import random
import string

# Parol uzunligini belgilash
length = int(input("Parol uzunligini kiriting: "))

# Harflar (katta va kichik), raqamlar va maxsus belgilarni yig'ish
characters = string.ascii_letters + string.digits + string.punctuation

# Tasodifiy belgilarni tanlab parol yasash
password = ''.join(random.choice(characters) for i in range(length))

print("Tasodifiy parol:", password)

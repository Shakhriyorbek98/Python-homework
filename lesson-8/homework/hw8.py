# 1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

try:
    a=int(input("Birinchi sonni kiriting"))
    b=int(input("Ikkinchi sonni kiriting"))

    result= a/b
    print("Natija:", result )

except ZeroDivisionError:
    print("Xato: Nolga teng bo'lishi mumkin emas!")


# 2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

try:
    x=int(input())
    print("Kiritilgan son -", x)

except ValueError:
    print("Xatolik")

# 3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

try:
    with open("lesson9example.txt", "r") as file_handler:
        print(file_handler.read())
except FileNotFoundError:
    print("Xatolik sodir bo'ldi!")

# 4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.

try:
    a=input("Number1:")
    b=input("Number2:")

    if not(a.isdigit() and b.isdigit()):
        raise TypeError("Faqat son kiriting!")
    a=int(a)
    b=int(b)

    print("Yig'indisi:", a+b)
except TypeError as e:
    print("Xato:", e)


# 5. Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.

try:
    filename=input("filename")
    with open("filename", "w") as file_handler:
        file_handler.write("Salom, bu sinov uchun edi\n")
        print("Fayl muvaffaqqiyatli yozildi.")
except PermissionError:
    print("There is a permission issue!")


# 6. Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.

try:
    my_list=["1", "2", "3"]
    print(my_list)

    index=int(input("Ro'yxattan tanlang"))

    print("Tanlandi:", my_list[index])
except IndexError:
    print("The index is out of range!")

# 7. Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.

try:
    son = int(input("Son kiriting"))
    print(son)
except KeyboardInterrupt:
    print("You cancelled the input")

# 8. Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.

try:
    a=int(input("Birinchi son"))
    b=int(input("Ikkinchi son"))

    result=a/b
    print(result)
except ArithmeticError:
    print("Xatolik yuz berdi")

# 9. Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.

try:
    with open("lesson9example.txt", "r") as file_handler:
        print(file_handler.read())
except UnicodeDecodeError:
    print("There is an encoding issue")

# 10. Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.

try:
    my_list=[7, 8, 9, 10]
    my_list.push(11)
except AttributeError :
    print("The attribute does not exist")



# Python File Input Output: Exercises, Practice, Solution

# 1. Write a Python program to read an entire text file.
try:
    with open("entiretextfile", "r") as file_handler:
        print(file_handler.read())
except:
    print("Error")

# 2. Write a Python program to read first n lines of a file.

def read_first_lines(filename, n):
    try:
        with open(filename, "r") as file_handler:
            lines=file_handler.readline()
            for line in lines[:n]:
                print(line.strip())
    except FileNotFoundError:
        print("Fayl mavjud emas!")

# 3. Write a Python program to append text to a file and display the text.

def append_and_display(filename,text):
    try:
        with open ("filename", "a") as file_handler1:
            filename.write(text+"\n")

        with open (filename, "r") as file_handler2:
            content=filename.read()
            print("Fayl maznmuni:\n")
            print(content)
    except Exception as e:
        print("Xatolik:", e)

# 4. Write a Python program to read last n lines of a file.

def read_last_n_lines(filename, n):
    try:
        with open(filename, "r") as file:
            # Barcha qatorlarni o‘qib olamiz
            lines = file.readlines()
            # Oxirgi n qatorni chiqaramiz
            last_lines = lines[-n:]
            print("Oxirgi", n, "qator:\n")
            for line in last_lines:
                print(line.strip())
    except FileNotFoundError:
        print("Fayl topilmadi.")
    except Exception as e:
        print("Xatolik:", e)


# Misol uchun foydalanish
read_last_n_lines("sample.txt", 3)


# 5.Write a Python program to read a file line by line and store it into a list.

def file_to_list(filename):
    try:
        with open(filename, "r") as file:
            # Fayldagi qatorlarni listga o‘qib olish
            lines = [line.strip() for line in file]
        return lines
    except FileNotFoundError:
        print("Fayl topilmadi.")
        return []
    except Exception as e:
        print("Xatolik:", e)
        return []


# Misol uchun foydalanish
lines_list = file_to_list("sample.txt")
print("Fayl ro‘yxat ko‘rinishida:\n", lines_list)


# 6.Write a Python program to read a file line by line and store it into a variable.

def file_to_string(filename):
    try:
        with open(filename, "r") as file:
            # Faylni qatorma-qator o‘qib bitta stringga yig‘amiz
            content = ""
            for line in file:
                content += line
        return content
    except FileNotFoundError:
        print("Fayl topilmadi.")
        return ""
    except Exception as e:
        print("Xatolik:", e)
        return ""


# Misol uchun foydalanish
text = file_to_string("sample.txt")
print("Fayldagi ma'lumot:\n", text)

# 7. Write a Python program to read a file line by line and store it into an array.

def file_to_array(filename):
    try:
        with open(filename, "r") as file:
            # Fayldagi qatorlarni array (list) ga o‘qib olamiz
            arr = file.readlines()
        return arr
    except FileNotFoundError:
        print("Fayl topilmadi.")
        return []
    except Exception as e:
        print("Xatolik:", e)
        return []


# Misol uchun foydalanish
array_data = file_to_array("sample.txt")
print("Fayl array ko‘rinishida:\n", array_data)


# 8. Write a Python program to find the longest words.

def find_longest_words(filename):
    try:
        with open(filename, "r") as file:
            words = file.read().split()  # matnni so‘zlarga bo‘lamiz
            max_len = max(len(word) for word in words)  # eng uzun so‘z uzunligini topamiz
            longest_words = [word for word in words if len(word) == max_len]  # eng uzun so‘zlarni yig‘amiz
        return longest_words
    except FileNotFoundError:
        print("Fayl topilmadi.")
        return []
    except Exception as e:
        print("Xatolik:", e)
        return []


# Misol uchun foydalanish
longest = find_longest_words("sample.txt")
print("Eng uzun so‘z(lar):", longest)


# 9. Write a Python program to count the number of lines in a text file.

def count_lines(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()   # barcha qatorlarni o‘qib olamiz
            return len(lines)          # uzunligini qaytaramiz
    except FileNotFoundError:
        print("Fayl topilmadi.")
        return 0
    except Exception as e:
        print("Xatolik:", e)
        return 0


# Misol uchun foydalanish
filename = "sample.txt"
line_count = count_lines(filename)
print(f"'{filename}' faylida {line_count} ta qator bor.")


# 10. Write a Python program to count the frequency of words in a file.

def word_frequency(filename):
    try:
        with open(filename, "r") as file:
            text = file.read().lower()          # fayldagi matnni o‘qib kichik harflarga o‘tkazamiz
            words = text.split()                # so‘zlarga bo‘lamiz
            freq = {}                           # bo‘sh lug‘at yaratamiz

            for word in words:
                # belgilarni tozalash (vergul, nuqta va h.k.)
                word = word.strip(".,!?;:\"'()[]{}")
                if word in freq:
                    freq[word] += 1
                else:
                    freq[word] = 1
        return freq
    except FileNotFoundError:
        print("Fayl topilmadi.")
        return {}
    except Exception as e:
        print("Xatolik:", e)
        return {}


# Misol uchun foydalanish
filename = "sample.txt"
result = word_frequency(filename)

print(f"'{filename}' faylidagi so‘z chastotasi:")
for word, count in result.items():
    print(f"{word}: {count}")


# 11. Write a Python program to get the file size of a plain file.

import os

def get_file_size(filename):
    try:
        size = os.path.getsize(filename)  # fayl o‘lchamini baytlarda olamiz
        return size
    except FileNotFoundError:
        print("Fayl topilmadi.")
        return None
    except Exception as e:
        print("Xatolik:", e)
        return None


# Misol uchun foydalanish
filename = "sample.txt"
size = get_file_size(filename)

if size is not None:
    print(f"'{filename}' fayl hajmi: {size} bayt")

# 12. Write a Python program to write a list to a file.

def write_list_to_file(filename, data_list):
    try:
        with open(filename, "w") as file:
            for item in data_list:
                file.write(str(item) + "\n")   # har bir elementni yangi qatorda yozamiz
        print(f"Ro'yxat '{filename}' fayliga yozildi.")
    except Exception as e:
        print("Xatolik:", e)


# Misol uchun foydalanish
my_list = ["Apple", "Banana", "Cherry", "Date"]
write_list_to_file("fruits.txt", my_list)

# 13. Write a Python program to copy the contents of a file to another file.

def copy_file(source, destination):
    try:
        with open(source, "r") as src:          # manba faylni o‘qish
            content = src.read()                # hamma matnni o‘qib olish

        with open(destination, "w") as dest:    # yangi faylni yozish
            dest.write(content)                 # mazmunini yozish

        print(f"'{source}' fayli '{destination}' fayliga nusxalandi.")
    except FileNotFoundError:
        print("Manba fayl topilmadi.")
    except Exception as e:
        print("Xatolik:", e)


# Misol uchun foydalanish
copy_file("sample.txt", "sample_copy.txt")


# 14. Write a Python program to combine each line from the first file with the corresponding line in the second file.

def combine_files(file1, file2, output_file):
    try:
        with open(file1, "r") as f1, open(file2, "r") as f2, open(output_file, "w") as out:
            for line1, line2 in zip(f1, f2):       # ikkita fayldan mos qatorlarni olish
                combined_line = line1.strip() + " " + line2   # qatorlarni birlashtirish
                out.write(combined_line)            # yangi faylga yozish

        print(f"'{file1}' va '{file2}' fayllari '{output_file}' fayliga birlashtirildi.")
    except FileNotFoundError:
        print("Fayllardan biri topilmadi.")
    except Exception as e:
        print("Xatolik:", e)


# Misol uchun foydalanish
combine_files("file1.txt", "file2.txt", "combined.txt")

# 15. Write a Python program to read a random line from a file.

import random

def read_random_line(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()   # barcha satrlarni o‘qish
            if not lines:             # agar fayl bo‘sh bo‘lsa
                return "Fayl bo‘sh!"
            return random.choice(lines).strip()   # tasodifiy satrni tanlash
    except FileNotFoundError:
        return "Fayl topilmadi!"
    except Exception as e:
        return f"Xatolik: {e}"


# Misol uchun foydalanish
print(read_random_line("sample.txt"))

# 16. Write a Python program to assess if a file is closed or not.

def check_file_status(filename):
    try:
        file = open(filename, "r")
        print("Fayl ochildi:", file.name)
        print("Fayl yopilganmi? ->", file.closed)  # False bo‘ladi
        file.close()
        print("Fayl yopilganmi? ->", file.closed)  # True bo‘ladi
    except FileNotFoundError:
        print("Fayl topilmadi!")
    except Exception as e:
        print("Xatolik:", e)


# Misol uchun
check_file_status("sample.txt")


# 17. Write a Python program to remove newline characters from a file.

def remove_newlines(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        # Yangi faylga yozish (yoki eski faylni qayta yozish)
        with open("cleaned_" + filename, "w") as file:
            for line in lines:
                file.write(line.strip() + " ")  # \n olib tashlanadi, so'zlar orasiga bo'sh joy qo'shildi

        print("Newline belgilar olib tashlandi! Natija 'cleaned_" + filename + "' faylida.")
    except FileNotFoundError:
        print("Fayl topilmadi!")
    except Exception as e:
        print("Xatolik:", e)


# Misol uchun
remove_newlines("sample.txt")


# 18. Write a Python program that takes a text file as input and returns the number of words in a given text file.

def count_words(filename):
    try:
        with open(filename, "r") as file:
            text = file.read()
            words = text.split()   # Bo'sh joy va yangi qatordan bo'lib olish
            return len(words)
    except FileNotFoundError:
        print("Fayl topilmadi!")
        return 0
    except Exception as e:
        print("Xatolik:", e)
        return 0


# Misol uchun
filename = "sample.txt"   # o'z faylingiz nomini yozing
print("So'zlar soni:", count_words(filename))

# 19. Write a Python program to extract characters from various text files and put them into a list.

def extract_characters(filenames):
    chars = []
    try:
        for file in filenames:
            with open(file, "r") as f:
                text = f.read()
                for ch in text:
                    chars.append(ch)   # har bir belgini ro'yxatga qo'shamiz
        return chars
    except FileNotFoundError:
        print("Fayl topilmadi!")
        return []
    except Exception as e:
        print("Xatolik:", e)
        return []


# Misol uchun
files = ["file1.txt", "file2.txt", "file3.txt"]  # o'z fayl nomlaringizni yozing
characters = extract_characters(files)
print("Barcha belgilar ro'yxati:", characters)


# 20. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.

import string

# string.ascii_uppercase -> 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for letter in string.ascii_uppercase:
    filename = f"{letter}.txt"
    with open(filename, "w") as f:
        f.write(f"This is file {filename}\n")  # fayl ichiga oddiy matn yozamiz

print("26 ta fayl muvaffaqiyatli yaratildi!")


# 21. Write a Python program to create a file where all letters of the English alphabet are listed with 
# a specified number of letters on each line.

import string

def create_alphabet_file(filename, per_line):
    letters = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    with open(filename, "w") as f:
        for i in range(0, len(letters), per_line):
            line = letters[i:i+per_line]  # bo‘laklab olish
            f.write(line + "\n")
    print(f"{filename} fayli yaratildi!")

# Misol: 5 ta harf bir qatorda
create_alphabet_file("alphabet.txt", 5)

# 1. Given a side of square. Find its perimeter and area.

# foydalanuvchidan kvadrat tomoni kiritiladi
side = float(input("Kvadrat tomoni: "))

perimeter = 4 * side
area = side * side

print("Perimetri:", perimeter)
print("Yuzi:", area)


# 2. Given diameter of circle. Find its length.


import math
diameter = float(input("Aylana diametri: "))
length = math.pi * diameter
print("Aylana uzunligi:", length)


# 3. Given two numbers a and b. Find their mean.

a=float(input("Birinchi son:"))
b=float(input("Ikkinchi son:"))

mean=(a+b)/2

print("O'rtacha qiymat:", mean)

# 4. Given two numbers a and b. Find their sum, product and square of each number.

a=float(input("Birinchi son:"))
b=float(input("Ikkinchi son:"))

sum=a+b
product=a*b
square_a =a**2
square_b=b**2

print("sum:", sum)
print("product:", product)
print("square_a:", square_a)
print("square_b:", square_b)

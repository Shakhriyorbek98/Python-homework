# lesson 16 homeworks

# 1. Convert List to 1D Array

import numpy as np

# Asl ro'yxat
list1 = [12.23, 13.32, 100, 36.32]
print("Original List:", list1)

# NumPy arrayga aylantirish
array1 = np.array(list1)
print("One-dimensional NumPy array:", array1)


# 2. Create 3x3 Matrix (2?10)

import numpy as np

# 2 dan 10 gacha sonlar yaratamiz
matrix = np.arange(2, 11).reshape(3, 3)

print(matrix)

# 3.Null Vector (10) & Update Sixth Value

import numpy as np

# 10 ta elementdan iborat null (nol) vektor
vector = np.zeros(10)
print("Original vector:", vector)

# 6-element (indeks 5) ni 11 ga o‘zgartirish
vector[5] = 11
print("Updated vector:", vector)


# 4. Array from 12 to 38
# Write a NumPy program to create an array with values ranging from 12 to 38.

import numpy as nb

array=nb.arange(12, 38)
print(array)


# 5. Convert Array to Float Type
# Write a NumPy program to convert an array to a floating type.

import numpy as np

# Asl array
arr = np.array([1, 2, 3, 4])
print("Original array:", arr)

# Float turiga o‘tkazish
float_arr = arr.astype(float)
print("Array converted to float:", float_arr)


# 6. Celsius to Fahrenheit Conversion
# Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees. Centigrade values are stored in a NumPy array.
# Sample Array [0, 12, 45.21, 34, 99.91] [-17.78, -11.11, 7.34, 1.11, 37.73, 0. ]

import numpy as np

# Celsius qiymatlar
celsius = np.array([0, 12, 45.21, 34, 99.91, 0.0])
print("Values in Celsius degrees:", celsius)

# Fahrenheit ga o‘tkazish
fahrenheit = celsius * 9/5 + 32
print("Values in Fahrenheit degrees:", fahrenheit)

# Fahrenheit dan yana Celsius ga qaytarish
celsius_converted = (fahrenheit - 32) * 5/9
print("Converted back to Celsius:", np.round(celsius_converted, 2))

# 7. Append Values to Array (Do self-tudy)
# Write a NumPy program to append values to the end of an array.

import numpy as np

# Boshlang‘ich massiv
arr = np.array([10, 20, 30])
print("Original array:", arr)

# Yangi qiymatlar qo‘shish
new_arr = np.append(arr, [40, 50, 60, 70, 80, 90])
print("After append values to the end of the array:", new_arr)


# 8. Array Statistical Functions (Do self-tudy)
# Create a random NumPy array of 10 elements and calculate the mean, median, and standard deviation of the array.


import numpy as np

# Tasodifiy 10 ta elementli massiv yaratamiz (0 dan 100 gacha)
arr = np.random.randint(0, 100, 10)
print("Array:", arr)

# Statistika hisoblash
mean = np.mean(arr)   # O‘rtacha qiymat
median = np.median(arr)  # Median
std_dev = np.std(arr)    # Standart og‘ish

print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)


# 9. Find min and max
# Create a 10x10 array with random values and find the minimum and maximum values.

import numpy as np

# 10x10 o‘lchamli tasodifiy array (0 dan 100 gacha)
arr = np.random.randint(0, 100, (10, 10))

print("Array:\n", arr)

# Minimum va maksimum qiymatlarni topish
min_val = np.min(arr)
max_val = np.max(arr)

print("\nMinimum qiymat:", min_val)
print("Maksimum qiymat:", max_val)


# 10. Create a 3x3x3 array with random values.

import numpy as np

# 3x3x3 o‘lchamli tasodifiy array (0 dan 1 gacha)
arr = np.random.random((3, 3, 3))

print("3x3x3 tasodifiy array:\n", arr)

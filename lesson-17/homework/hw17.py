# lesson 17 homeworks

# 1. Rename column names using function. "First Name" --> "first_name", "Age" --> "age

import pandas as pd

data ={
    'First Name':['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City':['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df=pd.DataFrame(data)

df=df.rename(columns={"First Name": "first_name", "Age":"age"})

print(df)

# 2. Print the first 3 rows of the DataFrame

import pandas as pd

# Ma'lumotlar
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Faqat dastlabki 3 qatorni chiqarish
print(df.head(3))

# 3. Find the mean age of the individuals

import pandas as pd

# Ma'lumotlar
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Yoshi o‘rtachasini hisoblash
mean_age = df['Age'].mean()

print("Mean age:", mean_age)


# 4. Select and print only the 'Name' and 'City' columns

import pandas as pd

# Ma'lumotlar
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Faqat 'First Name' va 'City' ustunlarini tanlash
selected_columns = df[['First Name', 'City']]

print(selected_columns)


# 5. Add a new column 'Salary' with random salary values

import pandas as pd
import numpy as np  # tasodifiy sonlar uchun

# Ma'lumotlar
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Yangi ustun: 'Salary' (tasodifiy qiymatlar 50000 dan 100000 gacha)
df['Salary'] = np.random.randint(50000, 100000, size=len(df))

print(df)


# 6. Display summary statistics of the DataFrame

import pandas as pd
import numpy as np

# Ma'lumotlar
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Yangi 'Salary' ustunini qo‘shamiz
df['Salary'] = np.random.randint(50000, 100000, size=len(df))

# DataFrame statistikasi
print(df.describe())


# Homework 2. 1. Create a DataFrame named sales_and_expenses with columns 
# 'Month', 'Sales', and 'Expenses', representing monthly sales and expenses data. Use below table.

import pandas as pd

# Ma'lumotlar lug'at shaklida
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}

# DataFrame yaratish
sales_and_expenses = pd.DataFrame(data)

# Natijani ko‘rsatish
print(sales_and_expenses)


# 2. Calculate and display the maximum sales and expenses.
# Maksimum qiymatlarni topish
max_sales = sales_and_expenses['Sales'].max()
max_expenses = sales_and_expenses['Expenses'].max()

# Natijani chiqarish
print("Maximum Sales:", max_sales)
print("Maximum Expenses:", max_expenses)


# 3. Calculate and display the minimum sales and expenses.

# Minimum qiymatlarni topish
min_sales = sales_and_expenses['Sales'].min()
min_expenses = sales_and_expenses['Expenses'].min()

# Natijani chiqarish
print("Minimum Sales:", min_sales)
print("Minimum Expenses:", min_expenses)

# 4. Calculate and display the average sales and expenses.

# O‘rtacha qiymatlarni hisoblash
avg_sales = sales_and_expenses['Sales'].mean()
avg_expenses = sales_and_expenses['Expenses'].mean()

# Natijani chiqarish
print("Average Sales:", avg_sales)
print("Average Expenses:", avg_expenses)


# Homework 3. 
# 1. Create a DataFrame named expenses with columns
# 'Category', 'January', 'February', 'March', and 'April', representing monthly expenses for different categories. Use below table.

import pandas as pd

# Ma'lumotlar jadvali
data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

# DataFrame yaratish
expenses = pd.DataFrame(data)

# Natijani chiqarish
print(expenses)


# 2. Calculate and display the maximum expense for each category.

import pandas as pd

# Ma'lumotlar jadvali
data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

# DataFrame yaratish
expenses = pd.DataFrame(data)

# Har bir kategoriya uchun maksimal xarajatni hisoblash
expenses['Max Expense'] = expenses[['January', 'February', 'March', 'April']].max(axis=1)

# Natijani chiqarish
print(expenses[['Category', 'Max Expense']])


# 3.  Calculate and display the minimum expense for each category.


import pandas as pd

# Ma'lumotlar jadvali
data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

# DataFrame yaratish
expenses = pd.DataFrame(data)

# Har bir kategoriya uchun minimal xarajatni hisoblash
expenses['Min Expense'] = expenses[['January', 'February', 'March', 'April']].min(axis=1)

# Natijani chiqarish
print(expenses[['Category', 'Min Expense']])



# 4. Calculate and display the average expense for each category.

import pandas as pd

# Ma'lumotlar jadvali
data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

# DataFrame yaratish
expenses = pd.DataFrame(data)

# Har bir kategoriya uchun o‘rtacha (average) xarajatni hisoblash
expenses['Average Expense'] = expenses[['January', 'February', 'March', 'April']].mean(axis=1)

# Natijani chiqarish
print(expenses[['Category', 'Average Expense']])





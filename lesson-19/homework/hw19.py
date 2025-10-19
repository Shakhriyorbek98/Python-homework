
# Homework 19

# Homework Assignment 1: Analyzing Sales Data

# You are given a dataset containing sales data for an e-commerce website. The dataset (task\sales_data.csv) has the following columns:

# Date: Date of the sale.
# Product: Name of the product sold.
# Category: Category to which the product belongs.
# Quantity: Number of units sold.
# Price: Price per unit.
# Tasks:

# 1. Group the data by the Category column and calculate the following aggregate statistics for each category:
# Total quantity sold.
# Average price per unit.
# Maximum quantity sold in a single transaction.

import pandas as pd

# CSV fayldan ma'lumotni o‘qish
df = pd.read_csv('task/sales_data.csv')

# Ma'lumotni ko‘rish (xohlasa)
print(df.head())

# Kategoriya bo‘yicha guruhlab, statistikalarni hisoblash
category_stats = df.groupby('Category').agg(
    Total_Quantity_Sold=('Quantity', 'sum'),        # umumiy miqdor
    Average_Price=('Price', 'mean'),                # o‘rtacha narx
    Max_Quantity_Single_Sale=('Quantity', 'max')    # eng katta tranzaksiya
)

# Natijani chiqarish
print("\nCategory-wise aggregate statistics:")
print(category_stats)


# 2. Identify the top-selling product in each category based on the total quantity sold.

import pandas as pd

# CSV faylni o‘qish
df = pd.read_csv('task/sales_data.csv')

# Har bir mahsulot bo‘yicha jami sotilgan miqdorni hisoblash
product_sales = df.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()

# Har bir kategoriya ichida eng ko‘p sotilgan mahsulotni topish
top_selling = product_sales.loc[product_sales.groupby('Category')['Quantity'].idxmax()]

# Natijani chiqarish
print("Top-selling product in each category:")
print(top_selling)



# 3. Find the date on which the highest total sales (quantity * price) occurred.

import pandas as pd

# CSV faylni o‘qish
df = pd.read_csv('task/sales_data.csv')

# Har bir qatordagi umumiy savdoni hisoblash
df['Total_Sales'] = df['Quantity'] * df['Price']

# Sana bo‘yicha jami savdoni hisoblash
daily_sales = df.groupby('Date')['Total_Sales'].sum()

# Eng katta savdo bo‘lgan sana
max_sales_date = daily_sales.idxmax()
max_sales_amount = daily_sales.max()

print(f"The highest total sales occurred on {max_sales_date} with total sales of {max_sales_amount:.2f}")


# Homework Assignment 2: Examining Customer Orders

# You have a dataset (task\customer_orders.csv) containing information about customer orders. The dataset has the following columns:

# OrderID: Unique identifier for each order.
# CustomerID: Unique identifier for each customer.
# Product: Name of the product ordered.
# Quantity: Number of units ordered.
# Price: Price per unit.
# Tasks:

# 1. Group the data by CustomerID and filter out customers who have made less than 20 orders.

import pandas as pd

# CSV faylni o‘qish
df = pd.read_csv('task/customer_orders.csv')

# Har bir mijoz nechta buyurtma qilganini hisoblash
order_counts = df.groupby('CustomerID')['OrderID'].nunique()

# 20 tadan ko‘p buyurtma qilgan mijozlar
active_customers = order_counts[order_counts >= 20].index

# Asosiy jadvaldan faqat shu mijozlarni qoldirish
filtered_df = df[df['CustomerID'].isin(active_customers)]

print(filtered_df)


# 2. Identify customers who have ordered products with an average price per unit greater than $120.
import pandas as pd

# CSV faylni o‘qish
df = pd.read_csv('task/customer_orders.csv')

# Har bir mijoz uchun o‘rtacha narxni hisoblash
avg_price_per_customer = df.groupby('CustomerID')['Price'].mean()

# O‘rtacha narxi 120 dan yuqori bo‘lgan mijozlarni tanlash
high_value_customers = avg_price_per_customer[avg_price_per_customer > 120]

print("Customers with average price per unit greater than $120:\n")
print(high_value_customers)


# 3. Find the total quantity and total price for each product ordered, and filter out products that have a total quantity less than 5 units.

import pandas as pd

# CSV faylni o‘qish
df = pd.read_csv('task/customer_orders.csv')

# Har bir mahsulot bo‘yicha jami miqdor va jami narxni hisoblash
product_summary = df.groupby('Product').agg(
    total_quantity=('Quantity', 'sum'),
    total_price=('Price', 'sum')
)

#  5 donadan kam sotilgan mahsulotlarni filtrlash
filtered_products = product_summary[product_summary['total_quantity'] >= 5]

print("Products with total quantity >= 5 units:\n")
print(filtered_products)

# Homework Assignment 3: Population Salary Analysis

# 3. "task\population.db" sqlite database has population table.


import sqlite3
import pandas as pd

# Bazaga ulanish
conn = sqlite3.connect('task/population.db')

# Ma’lumotlarni o‘qish
df = pd.read_sql_query("SELECT * FROM population", conn)

# Jadvalni ko‘rish
print(df.head())


salary_stats = df['salary'].agg(['mean', 'min', 'max'])
print("Salary statistics:")
print(salary_stats)


most_populous = df.loc[df['population'].idxmax()]
print("\nCountry with highest population:")
print(most_populous)

top_salaries = df.sort_values(by='salary', ascending=False).head(5)
print("\nTop 5 countries with highest average salary:")
print(top_salaries)

correlation = df['population'].corr(df['salary'])
print(f"\nCorrelation between population and salary: {correlation:.2f}")



# 2. "task\population salary analysis.xlsx" file defines Salary Band categories.
# Read the data from population table and calculate following measures:
# Percentage of population for each salary category;
# Average salary in each salary category;
# Median salary in each salary category;
# Number of population in each salary category;

import sqlite3
import pandas as pd

# 1️⃣ Bazadan ma'lumotlarni o‘qish
conn = sqlite3.connect('task/population.db')
population_df = pd.read_sql_query("SELECT * FROM population", conn)

# 2️⃣ Excel fayldan Salary Band jadvalini o‘qish
salary_band_df = pd.read_excel("task/population salary analysis.xlsx")

print("Salary band data:")
print(salary_band_df.head())

# 3️⃣ Salary band’larni population ma’lumotlariga moslashtirish
# Faraz qilamizki, Excel faylda ustunlar quyidagicha: ["Band", "Min_Salary", "Max_Salary"]
# Band nomi orqali qaysi kategoriya ekanini aniqlaymiz
def get_salary_band(salary):
    for _, row in salary_band_df.iterrows():
        if row["Min_Salary"] <= salary <= row["Max_Salary"]:
            return row["Band"]
    return "Unknown"

population_df["Salary_Band"] = population_df["salary"].apply(get_salary_band)

# 4️⃣ Har bir kategoriya uchun hisoblash
summary = population_df.groupby("Salary_Band").agg(
    Population_Count=('population', 'count'),
    Avg_Salary=('salary', 'mean'),
    Median_Salary=('salary', 'median')
).reset_index()

# 5️⃣ Foizni hisoblash
total_population = summary['Population_Count'].sum()
summary['Population_Percentage'] = (summary['Population_Count'] / total_population) * 100

# 6️⃣ Natijani chiqarish
print("\n=== Salary Band Analysis ===")
print(summary)

# 7️⃣ (ixtiyoriy) Natijani Excel faylga yozish
summary.to_excel("task/salary_band_summary.xlsx", index=False)
print("\n✅ Natija 'task/salary_band_summary.xlsx' fayliga yozildi.")


# 3. Calculate the same measures in each State

import sqlite3
import pandas as pd

# 1️⃣ Bazadan ma'lumotlarni o‘qish
conn = sqlite3.connect('task/population.db')
population_df = pd.read_sql_query("SELECT * FROM population", conn)

# 2️⃣ Excel fayldan Salary Band ma'lumotlarini o‘qish
salary_band_df = pd.read_excel("task/population salary analysis.xlsx")

# 3️⃣ Har bir oylikni to‘g‘ri bandga joylashtirish
def get_salary_band(salary):
    for _, row in salary_band_df.iterrows():
        if row["Min_Salary"] <= salary <= row["Max_Salary"]:
            return row["Band"]
    return "Unknown"

population_df["Salary_Band"] = population_df["salary"].apply(get_salary_band)

# 4️⃣ Har bir STATE ichida Salary Band bo‘yicha statistikalar
state_summary = (
    population_df
    .groupby(["State", "Salary_Band"])
    .agg(
        Population_Count=('population', 'count'),
        Avg_Salary=('salary', 'mean'),
        Median_Salary=('salary', 'median')
    )
    .reset_index()
)

# 5️⃣ Har bir STATE bo‘yicha umumiy sonni hisoblab, foizni qo‘shish
total_by_state = (
    state_summary.groupby("State")["Population_Count"].transform("sum")
)
state_summary["Population_Percentage"] = (
    (state_summary["Population_Count"] / total_by_state) * 100
)

# 6️⃣ Natijani chiqarish
print("\n=== Salary Band Analysis by State ===")
print(state_summary)

# 7️⃣ (ixtiyoriy) Excel faylga yozish
state_summary.to_excel("task/salary_band_by_state.xlsx", index=False)
print("\n✅ Natija 'task/salary_band_by_state.xlsx' fayliga yozildi.")




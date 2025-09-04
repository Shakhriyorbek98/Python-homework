############################### Homeworks of lesson 4

# 1. Sort a Dictionary by Value. Write a Python script to sort (ascending and descending) a dictionary by value.

my_dict={"chevrolet":"5", "Kia":"3", "Honda":"6"}
print(my_dict)

asc_sorting=dict(sorted(my_dict.items(), key=lambda item: item[1]))
desc_sorting=dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print(desc_sorting)

# 2. Add a Key to a Dictionary. Write a Python script to add a key to a dictionary.

my_dict={"0":"10", "1":"20"}
my_dict.update([("2","30")])
my_dict

# 3. Concatenate Multiple Dictionaries. Write a Python script to concatenate the following dictionaries to create a new one.

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

result = {}
result.update(dic1)
result.update(dic2)
result.update(dic3)
result


# 4. Generate a Dictionary with Squares. 
# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 

n=int(input())

squares = {}

for x in range(1, n+1):
    squares[x]=x*x

print(squares)


# 5. Dictionary of Squares (1 to 15). Write a Python script to print a dictionary where the keys are 
# numbers between 1 and 15 (both included) and the values are the square of the keys.

n=int(input())

squares ={}

for x in range(1, 16):
    squares[x]=x*x

print(squares)

############################################333SET EXERCISES

# 1. Create a Set. Write a Python program to create a set.

my_set={"a", "b", "c"}
type(my_set)

# 2. Iterate Over a Set. Write a Python program to iterate over sets.

mysecond_set={"fruits", "autos", "techs"}
for item in mysecond_set:
    print(item)

# 3. Add Member(s) to a Set. Write a Python program to add member(s) to a set.

second_set={"gas","oil","engine"}
print(second_set)
second_set.add("Members")
print("Element qushildi:", second_set)

# 4. Remove Item(s) from a Set. Write a Python program to remove item(s) from a given set.

second_set.remove("gas")

# 5. Remove an Item if Present in the Set. Write a Python program to remove an item from a set if it is present in the set.

my_set = {"apple", "banana", "cherry"}

print("Asl set:", my_set)

item = "banana"

my_set.discard(item)

print(f"{item} o'chirilgandan keyin:", my_set)

# 1. Create and Access List Elements. Create a list containing five different fruits and print the third fruit.

Fruits_list=["Apple", "Banana", "Cherry", "Ananas", "Coconut"]
print(Fruits_list)
type(Fruits_list)

# 2. Concatenate Two Lists. Create two lists of numbers and concatenate them into a single list.

firstgroup_list=['1','2','3','4']
secondgroup_list=['5','6','7','8']

type(firstgroup_list)
type(secondgroup_list)

print(firstgroup_list+secondgroup_list)


# 3. Extract Elements from a List. Given a list of numbers, extract the first, middle, and last elements 
# and store them in a new list.

numbers = [5, 10, 15, 20, 25, 30, 35]

print("Asl ro'yxat:", numbers)

first = numbers[0]
middle = numbers[len(numbers) // 2]
last = numbers[-1]
new_list = [first, middle, last]

print("Yangi ro'yxat:", new_list)


# 4. Convert List to Tuple. Create a list of your five favorite movies and convert it into a tuple.

favorite_movies_list=tuple(['Superma', 'Batman', 'Dr.House', 'Sherlock', '18 years'])
favorite_movies_list
type(favorite_movies_list)

# 5. Check Element in a List. Given a list of cities, check if "Paris" is in the list and print the result.

cities_list=['Paris', 'London', 'Kuala Lumpur', 'Tashkent', 'Beshkek']
type(cities_list)
element_to_check='Paris'

if element_to_check in cities_list:
    print(f"'{element_to_check}' found in the list.")
else:
    print(f"'{element_to_check}' not found in the list.")


# 6.Duplicate a List Without Using Loops. Create a list of numbers and duplicate it without using loops.

numbers_list=[1,2,3,4,5,6]
type(numbers_list)
numbers_list
numbers=numbers_list.copy()
numbers


# 7.  Swap First and Last Elements of a List. Given a list of numbers, swap the first and last elements.

numbers_list=[1,2,3,4,5]
print("Ruyxat", numbers_list)

numbers_list[0], numbers_list[-1] = numbers_list[-1], numbers_list[0]
print("Almashgan ruyxat:", numbers_list)


# 8. Slice a Tuple. Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.

numbers_tuple=('1','2','3','4','5','6','7','8','9','10')
type(numbers_tuple)

sliced_tuple=numbers_tuple[3:7]
print(sliced_tuple)


# 9. Count Occurrences in a List. Create a list of colors and count how many times "blue" appears in the list.

color_occur_list=['red', 'green', 'blue']
type(color_occur_list)

color_occur_list.count("blue")


# 10. Find the Index of an Element in a Tuple. Given a tuple of animals, find the index of "lion".

animals_tuple=("Zebra", 'Horse', 'Elephant', 'Lion')
type(animals_tuple)

animals_tuple.index("Lion")


# 11. Merge Two Tuples. Create two tuples of numbers and merge them into a single tuple.

tuple1=(1,2,3,4,5)
tuple2=(6,7,8,9,10)

print(tuple1+tuple2)

# 12. Find the Length of a List and Tuple. Given a list and a tuple, find and print their lengths.

given_list=[1,2,3,4,5]
given_tuple=(10, 20, 30)

print(len(given_list))
print(len(given_tuple))

# 13. Convert Tuple to List. Create a tuple of five numbers and convert it into a list.

my_tuple=(1,2,3,4,5)
type(my_tuple)
my_list=list(my_tuple)
type(my_list)

# 14. Find Maximum and Minimum in a Tuple. Given a tuple of numbers, find and print the maximum and minimum values.

my_tuple=(1,2,3,4,5)
type(my_tuple)

maximum=max(my_tuple)
minimum=max(my_tuple)
print(minimum, maximum)

# 15. Reverse a Tuple. Create a tuple of words and print it in reverse order.

tuple_words=("apple", "fresh", "camel", "none", "new")
type(tuple_words)

reversed_words=tuple_words[::-1]
print(reversed_words)

# 1. Modify String with Underscores. 
# Given a string txt, insert an underscore (_) after every third character. 
# If a character is a vowel or already has an underscore after it, shift the underscore placement to the next character. 
# No underscore should be added at the end.

my_txt="hello"
used_chars=["a", "e", "u", "i", "o"]
i=2
while i<len(my_txt)-1:
    if my_txt[i] not in used_chars:
        my_txt=my_txt[:i+1]+"_"+my_txt[i+1:]
        used_chars.append(my_txt[i])
        i+=4

        print(my_txt)

# Integer Squares Exercise
# Task2
# The provided code stub reads an integer, n, from STDIN. For all non-negative integers i where 0 <= i < n, print i^2.

n=int(input().strip())

for i in range(n):
    print(i**2)

# Loop-Based Exercises
# Exercise 1: Print first 10 natural numbers using a while loop

cnt=1
while cnt<=10:
   print(cnt)
   cnt+=1

# Exercise 2: Print the following pattern

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n=5
for i in range(1, n+1):
    for j in range (1, i+1):
        print(j,end=" ")
    print ()
    
# Exercise 3: Calculate sum of all numbers from 1 to a given number

n=11

Total=0
for i in range (1, 11):
    Total+=i
    print(Total)

# Exercise 4: Print multiplication table of a given number

n=int(input())

i=1
while i<10:
    print(n*i)
    i+=1

# Exercise 5: Display numbers from a list using a loop

numbers=[12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if 75<=num<=150:
        print(num)

# Exercise 6: Count the total number of digits in a number

x=75869
len(str(x))


# Exercise 7: Print reverse number pattern

n=5

for i in range (n, 0, -1):
    for j in range (i, 0, -1):
        print(j, end=" ")
    print()

# Exercise 8: Print list in reverse order using a loop

list1 = [10, 20, 30, 40, 50]

for i in reversed(list1):
    print(i)


# Exercise 9: Display numbers from -10 to -1 using a for loop


for i in range (-10, 0):
    print(i)

# Exercise 10: Display message “Done” after successful loop execution

for i in range (0, 5):
    print(i)
print("Done!")

# Exercise 11: Print all prime numbers within a range

start=25
end=50

print(f"Prime numbers between {start} and {end}:")

for num in range (start, end +1):
    if num>1:
        for i in range (2, int(num**0.5)+1):
            if num%i==0:
                break
        else:
            print(num)

# Exercise 12: Display Fibonacci series up to 10 terms

    n=10

a, b= 0, 1

print("Fibonacci sequence:")

for i in range (n):
    print(a, end=" ")
    a, b= b, a+b

# Exercise 13: Find the factorial of a given number

num = int(input())

factorial=1

for i in range (1, num+1):
    factorial *=i
print(f"{num}!={factorial}")


# 4. Return Uncommon Elements of Lists

def uncommon_elements(list1, list2):
    result = []
    
    # list1 da bor, lekin list2 da yo‘q
    for item in list1:
        if item not in list2:
            result.append(item)
    
    # list2 da bor, lekin list1 da yo‘q
    for item in list2:
        if item not in list1:
            result.append(item)
    
    return result

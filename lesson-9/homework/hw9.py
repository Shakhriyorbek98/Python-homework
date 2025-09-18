#  1. Circle Class

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area (self):
        return math.pi*(self.radius**2)
    
    def perimeter (self):
        return 2 * math.pi*self.radius
    
c1=Circle(5)
print(c1.radius)
print(c1.area())
print(c1.perimeter())

# 2. Person Class

from datetime import datetime
class Person:
    def __init__(self, name, country, dob):
        self.name=name
        self.country=country
        self.dob=datetime.strptime(dob, "%Y-%m-%d")
    
    def age (self):
        today=datetime.today()
        years=today.year-self.dob.year

        if (today.month, today.day)<(self.dob.month, self.dob.day):
            years-=1
        return years
    
p1=Person("Ali", "Uzbekistan", "2000-05-20")
print("Name:", p1.name)
print("Country:", p1.country)
print("Date of birth:", p1.dob.date())
print("Age", p1.age())
    

# 3. Calculator Class

class Calculator:
    def add(self, a, b):
        return a+b

    def subtract(self, a, b):
        return a-b
    
    def multiply (self, a, b):
        return a *b
    
    def divide(self, a, b):
        if b==0:
            return "Error: Division by zero is not allowed!" 
        return a/b
        
calc=Calculator()

print("Add:", calc.add(10, 5))
print("Subtract:", calc.subtract(10, 5))
print("Multiply:", calc.multiply(10, 5))
print("Divide:", calc.divide(10, 5))
print("Divide by zero:", calc.divide(10, 0))

# 4. Shape and Subclasses

import math

class Shape:
    def area(self):
        raise NotImplementedError("Area method must be implemented in subclass")
    
    def perimeter(self):
        raise NotImplementedError ("Perimeter method must be implemented in subclass")
    
class Square(Shape):
    def __init__(self, side):
        self.side=side

    def area(self):
        return self.side**2
    
    def perimeter(self):
        return 4*self.side
    
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a=a
        self.b=b
        self.c=c

    def perimeter(self):
        return self.a+self.b+self.c
    
    def area(self):
        s=self.perimeter()/2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
    
circle = Circle(5)
square = Square(4)
triangle = Triangle(3, 4, 5)

print("Circle: Area =", circle.area(), ", Perimeter =", circle.perimeter())
print("Square: Area =", square.area(), ", Perimeter =", square.perimeter())
print("Triangle: Area =", triangle.area(), ", Perimeter =", triangle.perimeter())

# 5. Binary Search Tree Class

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert qilish
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current, key):
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert(current.left, key)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert(current.right, key)
        # Agar teng bo‘lsa, hech nima qilinmaydi (duplikatga ruxsat bermaymiz)

    # Qidirish
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, current, key):
        if current is None:
            return False
        if current.key == key:
            return True
        elif key < current.key:
            return self._search(current.left, key)
        else:
            return self._search(current.right, key)

    # Daraxtni Inorder ko‘rinishda chiqarish (tekshirish uchun)
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)


# --- Foydalanish ---
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("Inorder traversal:", bst.inorder())  # Daraxtni chiqarish
print("Search 40:", bst.search(40))  # True
print("Search 100:", bst.search(100))  # False

# 6. Stack Data Structure

class Stack:
    def __init__(self):
        self.items = []  # bo‘sh ro‘yxat yaratamiz

    # Element qo‘shish
    def push(self, item):
        self.items.append(item)
        print(f"{item} stackga qo‘shildi")

    # Element olish
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack bo‘sh, pop mumkin emas!"

    # Yuqoridagi elementni ko‘rish
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack bo‘sh!"

    # Stack bo‘sh yoki yo‘qligini tekshirish
    def is_empty(self):
        return len(self.items) == 0

    # Stack o‘lchami
    def size(self):
        return len(self.items)


# --- Foydalanish ---
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Yuqoridagi element:", stack.peek())  # 30
print("Olingan element:", stack.pop())      # 30
print("Stack hajmi:", stack.size())         # 2
print("Stack bo‘shmi?", stack.is_empty())   # False


# 7. Linked List Data Structure

# Node (tugun) klassi
class Node:
    def __init__(self, data):
        self.data = data   # tugun qiymati
        self.next = None   # keyingi tugunga havola


# LinkedList klassi
class LinkedList:
    def __init__(self):
        self.head = None   # boshlang‘ich tugun yo‘q

    # Ro‘yxatni ko‘rsatish
    def display(self):
        current = self.head
        if not current:
            print("Ro‘yxat bo‘sh!")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Oxiriga tugun qo‘shish
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:   # agar ro‘yxat bo‘sh bo‘lsa
            self.head = new_node
        else:
            current = self.head
            while current.next:   # oxirgi tugungacha boramiz
                current = current.next
            current.next = new_node

    # Tugunni o‘chirish
    def delete(self, key):
        current = self.head

        # Birinchi tugun o‘chirilsa
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Keyingi tugunlarni qidirish
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print(f"{key} ro‘yxatda topilmadi!")
            return

        prev.next = current.next
        current = None


# --- Foydalanish ---
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)

print("Boshlang‘ich ro‘yxat:")
ll.display()

ll.delete(20)
print("20 o‘chirildi:")
ll.display()

ll.delete(100)  # mavjud bo‘lmagan tugun


# 8. Shopping Cart Class

class ShoppingCart:
    def __init__(self):
        self.items = {}  # {mahsulot_nomi: [narx, miqdor]}

    # Mahsulot qo‘shish
    def add_item(self, name, price, quantity=1):
        if name in self.items:
            self.items[name][1] += quantity  # mavjud bo‘lsa miqdorini oshiramiz
        else:
            self.items[name] = [price, quantity]

    # Mahsulotni o‘chirish
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
        else:
            print(f"{name} savatda yo‘q!")

    # Jami narx
    def calculate_total(self):
        total = 0
        for price, quantity in self.items.values():
            total += price * quantity
        return total

    # Savatni ko‘rsatish
    def show_cart(self):
        if not self.items:
            print("Savat bo‘sh!")
            return
        print("Savat tarkibi:")
        for name, (price, quantity) in self.items.items():
            print(f"{name} - {quantity} dona x {price} so‘m = {price * quantity} so‘m")
        print(f"Jami: {self.calculate_total()} so‘m")


# --- Foydalanish ---
cart = ShoppingCart()
cart.add_item("Olma", 5000, 3)
cart.add_item("Non", 3000, 2)
cart.add_item("Sut", 8000)

cart.show_cart()

cart.remove_item("Non")
print("\nNon o‘chirildi:")
cart.show_cart()


# 9. Stack with Display

class Stack:
    def __init__(self):
        self.stack = []

    # Element qo‘shish (push)
    def push(self, item):
        self.stack.append(item)
        print(f"{item} stackka qo‘shildi.")

    # Element olish (pop)
    def pop(self):
        if not self.is_empty():
            removed = self.stack.pop()
            print(f"{removed} stackdan o‘chirildi.")
            return removed
        else:
            print("Stack bo‘sh, pop qilinmaydi!")
            return None

    # Stackni ko‘rsatish
    def display(self):
        if not self.is_empty():
            print("Stack elementlari (yuqoridan pastga):")
            for item in reversed(self.stack):
                print(item)
        else:
            print("Stack bo‘sh!")

    # Stack bo‘shligini tekshirish
    def is_empty(self):
        return len(self.stack) == 0


# --- Foydalanish ---
s = Stack()
s.push(10)
s.push(20)
s.push(30)

s.display()

s.pop()
s.display()


# 10. Queue Data Structure

class Queue:
    def __init__(self):
        self.queue = []

    # Element qo‘shish (enqueue)
    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} navbatga qo‘shildi.")

    # Element chiqarish (dequeue)
    def dequeue(self):
        if not self.is_empty():
            removed = self.queue.pop(0)  # birinchi element chiqadi
            print(f"{removed} navbatdan o‘chirildi.")
            return removed
        else:
            print("Navbat bo‘sh, dequeue qilib bo‘lmaydi!")
            return None

    # Navbatni ko‘rsatish
    def display(self):
        if not self.is_empty():
            print("Navbat elementlari (oldidan oxiriga):")
            for item in self.queue:
                print(item)
        else:
            print("Navbat bo‘sh!")

    # Navbat bo‘shligini tekshirish
    def is_empty(self):
        return len(self.queue) == 0


# --- Foydalanish ---
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

q.dequeue()
q.display()


# 11. Bank Class

class Bank:
    def __init__(self):
        # mijozlar ma'lumotlari (account_number: balance)
        self.accounts = {}

    # Yangi hisob ochish
    def open_account(self, account_number, initial_balance=0):
        if account_number in self.accounts:
            print("Bu hisob raqami allaqachon mavjud!")
        else:
            self.accounts[account_number] = initial_balance
            print(f"Hisob raqami {account_number} ochildi. Boshlang‘ich balans: {initial_balance}")

    # Balansni ko‘rish
    def check_balance(self, account_number):
        if account_number in self.accounts:
            print(f"Hisob {account_number} balans: {self.accounts[account_number]}")
            return self.accounts[account_number]
        else:
            print("Bunday hisob mavjud emas!")
            return None

    # Pul qo‘yish
    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            print(f"{amount} so‘m {account_number} hisobiga qo‘yildi.")
        else:
            print("Bunday hisob mavjud emas!")

    # Pul yechish
    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                print(f"{amount} so‘m {account_number} hisobidan olindi.")
            else:
                print("Balansda yetarli mablag‘ yo‘q!")
        else:
            print("Bunday hisob mavjud emas!")

    # Barcha hisoblarni ko‘rish
    def display_accounts(self):
        print("Bankdagi barcha hisoblar:")
        for acc, bal in self.accounts.items():
            print(f"Hisob raqami: {acc}, Balans: {bal}")


# --- Foydalanish ---
bank = Bank()

bank.open_account("12345", 500)
bank.open_account("67890", 1000)

bank.deposit("12345", 200)
bank.withdraw("67890", 300)

bank.check_balance("12345")
bank.check_balance("67890")

bank.display_accounts()

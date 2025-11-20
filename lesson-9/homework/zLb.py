1. Circle Class
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)


c = Circle(5)
print(c.area())
print(c.perimeter())

2. Person Class (age calculation)
from datetime import date, datetime

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = datetime.strptime(dob, "%Y-%m-%d").date()

    def age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))


p = Person("Ali", "Uzbekistan", "2000-05-10")
print(p.age())

3. Calculator Class
class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b


calc = Calculator()
print(calc.add(5, 3))

4. Shape + Subclasses
class Shape:
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        import math
        return math.pi * self.r**2

    def perimeter(self):
        import math
        return 2 * math.pi * self.r


class Square(Shape):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a**2

    def perimeter(self):
        return 4 * self.a


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def area(self):
        # Heron's formula
        s = (self.a + self.b + self.c) / 2
        return (s * (s-self.a)*(s-self.b)*(s-self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c

5. Binary Search Tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        def _insert(node, val):
            if not node:
                return Node(val)
            if val < node.val:
                node.left = _insert(node.left, val)
            else:
                node.right = _insert(node.right, val)
            return node

        self.root = _insert(self.root, val)

    def search(self, val):
        def _search(node, val):
            if not node:
                return False
            if val == node.val:
                return True
            return _search(node.left, val) if val < node.val else _search(node.right, val)

        return _search(self.root, val)

6. Stack Class
class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop() if self.items else None

7. Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        n = Node(data)
        n.next = self.head
        self.head = n

    def delete(self, key):
        cur = self.head
        prev = None

        while cur and cur.data != key:
            prev = cur
            cur = cur.next

        if not cur:
            return

        if not prev:
            self.head = cur.next
        else:
            prev.next = cur.next

    def display(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next

8. Shopping Cart
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, name, price):
        self.items.append((name, price))

    def remove(self, name):
        self.items = [i for i in self.items if i[0] != name]

    def total(self):
        return sum(price for _, price in self.items)

9. Stack with Display
class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop() if self.items else None

    def display(self):
        print(self.items)

10. Queue Data Structure
class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, x):
        self.q.append(x)

    def dequeue(self):
        return self.q.pop(0) if self.q else None

11. Bank Class
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, balance=0):
        self.accounts[name] = balance

    def deposit(self, name, amount):
        self.accounts[name] += amount

    def withdraw(self, name, amount):
        if self.accounts[name] < amount:
            raise ValueError("Insufficient funds")
        self.accounts[name] -= amount

    def get_balance(self, name):
        return self.accounts[name]

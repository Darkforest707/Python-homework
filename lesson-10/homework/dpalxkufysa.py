HOMEWORK 1 — ToDo List Application
Full OOP + CLI Version
from datetime import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✓ Done" if self.completed else "✗ Not Done"
        return f"{self.title} | {self.description} | Due: {self.due_date.date()} | {status}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_complete(self, title):
        for t in self.tasks:
            if t.title == title:
                t.mark_complete()
                return True
        return False

    def list_all(self):
        return self.tasks

    def list_incomplete(self):
        return [t for t in self.tasks if not t.completed]


def main():
    todo = ToDoList()

    while True:
        print("\n--- ToDo Menu ---")
        print("1. Add task")
        print("2. Mark task complete")
        print("3. List all tasks")
        print("4. List incomplete tasks")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            title = input("Title: ")
            desc = input("Description: ")
            due = input("Due date (YYYY-MM-DD): ")
            todo.add_task(Task(title, desc, due))
            print("Task added.")

        elif choice == "2":
            title = input("Enter task title to mark complete: ")
            if todo.mark_complete(title):
                print("Task completed.")
            else:
                print("Task not found.")

        elif choice == "3":
            for t in todo.list_all():
                print(t)

        elif choice == "4":
            for t in todo.list_incomplete():
                print(t)

        elif choice == "5":
            break

        else:
            print("Invalid option.")
            

if __name__ == "__main__":
    main()

HOMEWORK 2 — Simple Blog System
Full OOP Implementation + CLI + Edit/Delete features
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"{self.title} | by {self.author}\n{self.content}"


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        return self.posts

    def list_by_author(self, author):
        return [p for p in self.posts if p.author == author]

    def delete_post(self, title):
        self.posts = [p for p in self.posts if p.title != title]

    def edit_post(self, title, new_content):
        for p in self.posts:
            if p.title == title:
                p.content = new_content

    def latest_posts(self, n=5):
        return self.posts[-n:]


def main():
    blog = Blog()

    while True:
        print("\n--- Blog Menu ---")
        print("1. Add post")
        print("2. List posts")
        print("3. List by author")
        print("4. Edit post")
        print("5. Delete post")
        print("6. Latest posts")
        print("7. Exit")

        choice = input("Choose: ")

        if choice == "1":
            t = input("Title: ")
            c = input("Content: ")
            a = input("Author: ")
            blog.add_post(Post(t, c, a))
            print("Post added.")

        elif choice == "2":
            for p in blog.list_posts():
                print("\n", p)

        elif choice == "3":
            a = input("Author name: ")
            for p in blog.list_by_author(a):
                print("\n", p)

        elif choice == "4":
            t = input("Title to edit: ")
            new_c = input("New content: ")
            blog.edit_post(t, new_c)
            print("Post updated.")

        elif choice == "5":
            t = input("Title to delete: ")
            blog.delete_post(t)
            print("Post deleted.")

        elif choice == "6":
            for p in blog.latest_posts():
                print("\n", p)

        elif choice == "7":
            break

        else:
            print("Invalid option.")
            

if __name__ == "__main__":
    main()

HOMEWORK 3 — Simple Banking System
Full Bank System + Transfers + Overdraft Handling
class Account:
    def __init__(self, acc_number, holder, balance=0):
        self.acc_number = acc_number
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def __str__(self):
        return f"{self.acc_number} | {self.holder} | Balance: {self.balance}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, acc):
        self.accounts[acc.acc_number] = acc

    def get_account(self, acc_num):
        return self.accounts.get(acc_num, None)

    def transfer(self, from_acc, to_acc, amount):
        fa = self.get_account(from_acc)
        ta = self.get_account(to_acc)

        if not fa or not ta:
            raise ValueError("Account not found")

        fa.withdraw(amount)
        ta.deposit(amount)


def main():
    bank = Bank()

    while True:
        print("\n--- Bank Menu ---")
        print("1. Add account")
        print("2. Check balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            num = input("Account number: ")
            name = input("Holder name: ")
            bank.add_account(Account(num, name))
            print("Account created.")

        elif choice == "2":
            num = input("Account number: ")
            acc = bank.get_account(num)
            print(acc if acc else "Not found")

        elif choice == "3":
            num = input("Account number: ")
            amount = float(input("Amount: "))
            bank.get_account(num).deposit(amount)
            print("Deposited.")

        elif choice == "4":
            num = input("Account number: ")
            amount = float(input("Amount: "))
            try:
                bank.get_account(num).withdraw(amount)
                print("Withdrawn.")
            except ValueError as e:
                print(e)

        elif choice == "5":
            from_acc = input("From: ")
            to_acc = input("To: ")
            amount = float(input("Amount: "))
            try:
                bank.transfer(from_acc, to_acc, amount)
                print("Transferred.")
            except ValueError as e:
                print(e)

        elif choice == "6":
            break

        else:
            print("Invalid option.")
            

if __name__ == "__main__":
    main()

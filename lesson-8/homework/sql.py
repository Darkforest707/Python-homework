EXCEPTION HANDLING — SOLUTIONS
1. Handle ZeroDivisionError
try:
    a = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

2. Raise ValueError if input is not integer
try:
    x = input("Enter an integer: ")
    num = int(x)
except ValueError:
    print("Error: That is not an integer!")

3. Handle FileNotFoundError
try:
    f = open("not_existing.txt")
except FileNotFoundError:
    print("Error: File not found.")

4. Raise TypeError if input is not numerical
try:
    a = input("Enter number: ")
    b = input("Enter number: ")

    if not (a.replace('.', '').isdigit() and b.replace('.', '').isdigit()):
        raise TypeError("Inputs must be numbers")

    a, b = float(a), float(b)
except TypeError as e:
    print("Error:", e)

5. Handle PermissionError
try:
    f = open("/root/secret.txt")
except PermissionError:
    print("Error: Permission denied.")

6. Handle IndexError
lst = [1, 2, 3]

try:
    print(lst[5])
except IndexError:
    print("Error: Index out of range.")

7. Handle KeyboardInterrupt
try:
    x = input("Enter a number: ")
except KeyboardInterrupt:
    print("\nInput cancelled by user.")

8. Handle ArithmeticError
try:
    result = 10 / 0
except ArithmeticError:
    print("Arithmetic error occurred.")

9. Handle UnicodeDecodeError
try:
    f = open("file.txt", encoding="ascii")
    text = f.read()
except UnicodeDecodeError:
    print("Encoding error: Cannot decode file.")

10. Handle AttributeError
lst = [1, 2, 3]

try:
    lst.push(5)
except AttributeError:
    print("Error: List object has no such attribute.")

FILE INPUT / OUTPUT — SOLUTIONS

Assume we have a file: "sample.txt"

1. Read entire file
with open("sample.txt") as f:
    print(f.read())

2. Read first n lines
def read_first_n(filename, n):
    with open(filename) as f:
        for _ in range(n):
            print(f.readline().rstrip())

3. Append text to file + display
with open("sample.txt", "a") as f:
    f.write("\nNew line added!")

with open("sample.txt") as f:
    print(f.read())

4. Read last n lines
def read_last_n(filename, n):
    with open(filename) as f:
        print("".join(f.readlines()[-n:]))

5. Read file line by line → list
with open("sample.txt") as f:
    lines = f.readlines()
print(lines)

6. Read file line by line → variable
text = ""
with open("sample.txt") as f:
    for line in f:
        text += line

7. Read file line by line → array (list)

(Same as #5)

with open("sample.txt") as f:
    arr = [line for line in f]

8. Find longest words
with open("sample.txt") as f:
    words = f.read().split()
    max_len = max(len(word) for word in words)
    longest = [w for w in words if len(w) == max_len]
print(longest)

9. Count number of lines
with open("sample.txt") as f:
    print(len(f.readlines()))

10. Count frequency of words
from collections import Counter

with open("sample.txt") as f:
    words = f.read().split()
    print(Counter(words))

11. Get file size
import os
print(os.path.getsize("sample.txt"))

12. Write a list to file
lst = ["apple", "banana", "cherry"]

with open("list.txt", "w") as f:
    for x in lst:
        f.write(x + "\n")

13. Copy contents of one file to another
with open("sample.txt") as f1, open("copy.txt", "w") as f2:
    f2.write(f1.read())

14. Combine line-by-line from two files
with open("file1.txt") as f1, open("file2.txt") as f2:
    for a, b in zip(f1, f2):
        print(a.strip(), b.strip())

15. Read random line
import random

with open("sample.txt") as f:
    lines = f.readlines()
    print(random.choice(lines))

16. Check if file is closed
f = open("sample.txt")
print(f.closed)  # False
f.close()
print(f.closed)  # True

17. Remove newline characters
with open("sample.txt") as f:
    cleaned = [line.rstrip("\n") for line in f]

18. Count number of words (commas allowed)
with open("sample.txt") as f:
    text = f.read().replace(",", " ")
    words = text.split()
    print(len(words))

19. Extract characters from multiple files
import glob

chars = []
for filename in glob.glob("*.txt"):
    with open(filename) as f:
        chars.extend(list(f.read()))

print(chars)

20. Generate A.txt → Z.txt
import string

for letter in string.ascii_uppercase:
    open(f"{letter}.txt", "w").close()

21. Create file with alphabet, N letters per line
import string

def alphabet_file(n):
    letters = string.ascii_lowercase
    with open("alphabet.txt", "w") as f:
        for i in range(0, len(letters), n):
            f.write(letters[i:i+n] + "\n")

alphabet_file(5)

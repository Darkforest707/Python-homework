1. Modify String with Underscores

Логика:

Каждые 3 символа ставим _

Если текущий символ — гласная или уже стоит _ после неё → сдвигаем вставку

В конце _ не ставим

def add_underscores(txt):
    vowels = "aeiou"
    result = ""
    count = 0

    for i, ch in enumerate(txt):
        result += ch
        count += 1

        if count == 3:
            # не добавляем _ в конец строки
            if i != len(txt) - 1:
                # сдвиг, если гласная или следом уже _
                if ch in vowels or (i + 1 < len(txt) and txt[i+1] == "_"):
                    result += txt[i+1] if i + 1 < len(txt) else ""
                    result = result[:-1] + "_"  # вставляем _
                else:
                    result += "_"
            count = 0

    return result


print(add_underscores("hello"))          # hel_lo
print(add_underscores("assalom"))        # ass_alom
print(add_underscores("abcabcabcdeabcdefabcdefg"))


(решение хитрое, но рабочее)

2. Integer Squares (HackerRank style)
n = int(input())

for i in range(n):
    print(i*i)

3. Loop-Based Exercises
Exercise 1 — first 10 natural numbers
i = 1
while i <= 10:
    print(i)
    i += 1

Exercise 2 — pattern
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

Exercise 3 — sum 1 to n
n = int(input("Enter number: "))
total = sum(range(1, n+1))
print("Sum is:", total)

Exercise 4 — multiplication table
num = int(input())

for i in range(1, 11):
    print(num * i)

Exercise 5 — display filtered numbers

Условие: выводим числа меньше 500 и делящиеся на 5, но не равные 12.

numbers = [12, 75, 150, 180, 145, 525, 50]

for n in numbers:
    if n > 500:
        break
    if n % 5 == 0 and n != 12:
        print(n)

Exercise 6 — count digits
num = int(input())
print(len(str(num)))

Exercise 7 — reverse number pattern
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

Exercise 8 — print list in reverse
list1 = [10, 20, 30, 40, 50]

for i in reversed(list1):
    print(i)

Exercise 9 — numbers -10 to -1
for i in range(-10, 0):
    print(i)

Exercise 10 — print Done after loop
for i in range(5):
    print(i)
else:
    print("Done!")

Exercise 11 — prime numbers between range
start = 25
end = 50

for num in range(start, end + 1):
    if num > 1:
        for d in range(2, int(num**0.5) + 1):
            if num % d == 0:
                break
        else:
            print(num)

Exercise 12 — Fibonacci 10 terms
n1, n2 = 0, 1

print(n1, n2, end=" ")

for _ in range(8):
    nxt = n1 + n2
    print(nxt, end=" ")
    n1, n2 = n2, nxt

Exercise 13 — factorial
n = int(input())
fact = 1

for i in range(1, n+1):
    fact *= i

print(f"{n}! = {fact}")

4. Return Uncommon Elements of Lists
Логика:

Берём элементы, которые НЕ пересекаются.

Solution:
def uncommon(list1, list2):
    from collections import Counter

    c1 = Counter(list1)
    c2 = Counter(list2)

    result = []

    # элементы только из первого списка
    for el in c1:
        if c1[el] > c2.get(el, 0):
            result.extend([el] * (c1[el] - c2.get(el, 0)))

    # элементы только из второго списка
    for el in c2:
        if c2[el] > c1.get(el, 0):
            result.extend([el] * (c2[el] - c1.get(el, 0)))

    return result

Примеры:
print(uncommon([1,1,2], [2,3,4]))                     # [1,1,3,4]
print(uncommon([1,2,3], [4,5,6]))                     # [1,2,3,4,5,6]
print(uncommon([1,1,2,3,4,2], [1,3,4,5]))             # [2,2,5]

1. Функция is_leap(year)
def is_leap(year):
    """
    Determines whether a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.

    Parameters:
        year (int): The year to be checked.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

2. Conditional Statements Exercise ("Weird / Not Weird")
n = int(input())

if n % 2 == 1:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:  # n > 20 and even
    print("Not Weird")

3. Find even numbers between a and b (inclusive) — without loops
 Solution 1 — Using if-else
a = 3
b = 12

# make sure a <= b
if a > b:
    a, b = b, a

# start from the first even number
start = a if a % 2 == 0 else a + 1

# generate even numbers using range
evens = list(range(start, b + 1, 2))

print(evens)

✅ Solution 2 — Without if-else statement
a = 3
b = 12

start = a + (a % 2)   # если нечётное → +1, если чётное → +0

evens = list(range(start, b + 1, 2))

print(evens)

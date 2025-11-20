MAP va FILTER — Oddiy Tushuntirish + Misollar
1. map(function, iterable)

map — ro‘yxatning har bir elementiga bir xil funksiyani qo‘llaydi.

Misol (lambda bilan):
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x*x, numbers))
print(squared)  # [1, 4, 9, 16, 25]

2. filter(function, iterable)

filter — berilgan shartni qanoatlantiradigan elementlarni OLADI, boshqalarini tashlaydi.

Misol (lambda bilan):
numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)  # [2, 4, 6]

ENDII HOMEWORK SOLUTIONS
1. is_prime(n) funksiyasi
def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

Misollar:
print(is_prime(4))  # False
print(is_prime(7))  # True

2. digit_sum(k) funksiyasi
Variant 1 — oddiy
def digit_sum(k):
    return sum(int(digit) for digit in str(k))

Variant 2 — map bilan
def digit_sum(k):
    return sum(map(int, str(k)))

Misollar:
print(digit_sum(24))   # 6
print(digit_sum(502))  # 7

3. 2 ning darajalari (N dan katta bo‘lmagan)
def powers_of_two(N):
    k = 1
    result = []
    
    while k <= N:
        result.append(k)
        k *= 2
    
    return result

Misol:
print(*powers_of_two(10))  
# Output: 2 4 8

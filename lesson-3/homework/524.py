1. Create and Access List Elements
fruits = ["apple", "banana", "orange", "mango", "grape"]
print(fruits[2])
2. Concatenate Two Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print(result)
3. Extract Elements from a List
numbers = [10, 20, 30, 40, 50]
first = numbers[0]
middle = numbers[len(numbers)//2]
last = numbers[-1]
new_list = [first, middle, last]
print(new_list)
4. Convert List to Tuple
movies = ["Inception", "Interstellar", "Avatar", "Gladiator", "Shrek"]
movies_tuple = tuple(movies)
print(movies_tuple)
5. Check Element in List
cities = ["London", "Paris", "Madrid", "Berlin"]
print("Paris" in cities)
6. Duplicate a List Without Loops
nums = [1, 2, 3]
duplicated = nums * 2
print(duplicated)
7. Swap First and Last Elements
nums = [10, 20, 30, 40]
nums[0], nums[-1] = nums[-1], nums[0]
print(nums)
8. Slice a Tuple
t = (1,2,3,4,5,6,7,8,9,10)
print(t[3:8])
9. Count Occurrences
colors = ["blue", "red", "blue", "green", "blue"]
print(colors.count("blue"))
10. Find Index in Tuple
animals = ("cat", "dog", "lion", "tiger")
print(animals.index("lion"))
11. Merge Two Tuples
a = (1,2,3)
b = (4,5,6)
merged = a + b
print(merged)
12. Length of List and Tuple
lst = [1,2,3,4]
tpl = (10,20,30)
print(len(lst), len(tpl))
13. Convert Tuple to List
nums = (5, 10, 15, 20, 25)
converted = list(nums)
print(converted)
14. Max and Min in Tuple
numbers = (10, 200, 5, 99, 300)
print(max(numbers), min(numbers))
15. Reverse a Tuple
words = ("hello", "world", "python", "rules")
print(words[::-1])

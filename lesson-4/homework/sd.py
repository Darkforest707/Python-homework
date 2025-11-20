DICTIONARY EXERCISES
1. Sort a Dictionary by Value (ascending & descending)
data = {'a': 3, 'b': 1, 'c': 2}

# ascending
ascending = dict(sorted(data.items(), key=lambda x: x[1]))

# descending
descending = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
print("Ascending:", ascending)
print("Descending:", descending)

2. Add a Key to a Dictionary
d = {0: 10, 1: 20}
d[2] = 30
print(d)
3. Concatenate Multiple Dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
merged = {}
merged.update(dic1)
merged.update(dic2)
merged.update(dic3)
print(merged)
(можно и одной строкой: merged = {**dic1, **dic2, **dic3})

4. Generate a Dictionary with Squares (1 to n)
n = 5
result = {x: x*x for x in range(1, n+1)}
print(result)

5. Dictionary of Squares (1 to 15)
squares = {x: x*x for x in range(1, 16)}
print(squares)

SET EXERCISES
1. Create a Set
my_set = {1, 2, 3, 4}
print(my_set)

2. Iterate Over a Set
my_set = {"apple", "banana", "cherry"}
for item in my_set:
    print(item)

3. Add Member(s) to a Set
s = {1, 2, 3}
s.add(4)          # add one element
s.update([5, 6])  # add multiple elements
print(s)

4. Remove Item(s) from a Set
s = {10, 20, 30, 40}
s.remove(20)      # removes specific item
s.discard(30)     # also removes but doesn't give error
print(s)

5. Remove an Item if Present
s = {100, 200, 300}
if 200 in s:
    s.remove(200)
print(s)

d = {'a': 3, 'b': 1, 'c': 2}

# Ascending order
asc = dict(sorted(d.items(), key=lambda item: item[1]))
print("Ascending:", asc)

# Descending order
desc = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
print("Descending:", desc)

d = {'name': 'Sayali', 'age': 19}

key = 'age'

if key in d:
    print("Key exists")
else:
    print("Key does not exist")
    
    d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

d1.update(d2)

print("Merged Dictionary:", d1)

t = (1, 2, 3)

# Adding item
t = t + (4,)

print("Updated Tuple:", t)

t = (10, "Python", 3.14, True)

print("Tuple with different data types:", t)

numbers = [10, 20, 30, 40]

total = sum(numbers)

print("Sum of list items:", total)

numbers = [12, 45, 7, 89, 34]

largest = max(numbers)

print("Largest number:", largest)

s = {1, 2, 3}

# Add single item
s.add(4)

# Add multiple items
s.update([5, 6])

print("Updated Set:", s)


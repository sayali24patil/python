# 1. Create a tuple and perform basic operations

t1 = (10, 20, 30, 40)

print("Tuple:", t1)

# Length
print("Length of tuple:", len(t1))

# Concatenation
t2 = (50, 60)
print("Concatenation:", t1 + t2)

# Repetition
print("Repetition:", t1 * 2)

# Membership
print("Is 20 present?", 20 in t1)
print("Is 100 present?", 100 in t1)

# 2. Demonstrate indexing, negative indexing,
# slicing, and iteration on a tuple

t = ("Python", "Java", "C", "C++", "HTML")

# Indexing
print("First element:", t[0])

# Negative Indexing
print("Last element:", t[-1])

# Slicing
print("Elements from index 1 to 3:", t[1:4])

# Iteration
print("Iterating through tuple:")
for item in t:
    print(item)
    
# 3. Show that tuples are immutable
# and demonstrate tuple deletion using del

t = (1, 2, 3, 4)

print("Original tuple:", t)

# Tuples are immutable
# t[0] = 10   # This will give an error

print("Tuples cannot be modified.")

# Deleting tuple
del t

print("Tuple deleted successfully.")

# 4. Apply built-in tuple functions

numbers = (5, 10, 15, 20, 25)

# len()
print("Length:", len(numbers))

# max()
print("Maximum value:", max(numbers))

# min()
print("Minimum value:", min(numbers))

# tuple()
list_data = [1, 2, 3, 4]
new_tuple = tuple(list_data)

print("Tuple created using tuple():", new_tuple)
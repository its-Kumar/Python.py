numbers = [1, 2, 3, 4, 5, 6]

# normal
even = []
for n in numbers:
    if n % 2 == 0:
        even.append(n)

print(even)

# list Comprehension
even = [n for n in numbers if n % 2 == 0]
print(even)

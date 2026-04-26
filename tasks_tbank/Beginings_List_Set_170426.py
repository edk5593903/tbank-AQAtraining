# Список
numbers = [3, 1, 4, 1, 5, 9]
for n in numbers:
    print(n)

# Словарь
counts = {}
for n in numbers:
    counts[n] = counts.get(n, 0) + 1
print(counts)  # {3:1, 1:2, 4:1, 5:1, 9:1}
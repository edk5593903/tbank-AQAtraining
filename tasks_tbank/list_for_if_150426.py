figures = [1, 3, 3, 2, 5, 5, 5, 2, 1, 3, 1]
counts = {}

for figure in figures:
    counts[figure] = counts.get(figure, 0) + 1

max_counts = max(counts.values())

result = None
for key, value in counts.items():
    if value == max_counts:
        result = key
print(result)
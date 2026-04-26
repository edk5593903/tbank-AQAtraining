"""Есть список чисел: numbers = [1, 2, 3, 4, 2, 5, 6, 1, 7].
Напиши код на Python, который найдет и выведет в консоль все числа, 
которые встречаются в этом списке больше одного раза."""

numbers = [1, 2, 3, 4, 2, 5, 6, 1, 7]

repeats = {}
for digit in numbers:
    repeats[digit] = repeats.get(digit, 0) +1

result = None
for k, v in repeats.items():
    if v > 1:
        result = k
        print (result)
""" Есть список чисел: nums = [2, 7, 11, 15] и 
число-цель target = 9.
Нужно найти в списке два числа, которые в 
сумме дают target, и вывести их индексы."""

nums = [2, 7, 11, 15]
target = 9

# Внешний цикл (перебирает индексы)
for i in range(len(nums)): 
    """ Внутренний цикл (перебирает индексы 
    СЛЕДУЮЩИХ чисел)"""
    for j in range(i + 1, len(nums)):
        # 1. Сложи nums[i] и nums[j]
        addition = nums[i] + nums[j]
        """ 2. Если сумма равна target, выведи 
        i и j (индексы)"""
        if addition == target:
            print(i, j)

# 
nums = [2, 7, 11, 15]
target = 9
prev_values = {} # Наш словарь для "памяти"

for i, n in enumerate(nums): # enumerate дает и индекс (i), и само число (n)
    diff = target - n # Ищем, "сколько не хватает"
    
    if diff in prev_values:
        # Если "недостающее число" уже было — выводим индексы
        print(prev_values[diff], i)
        
    else:
        # Если еще не видели — записываем текущее число в словарь
        # Ключ — само число, Значение — его индекс i
        # ТВОЙ КОД ЗДЕСЬ (запиши число n в словарь prev_values под индексом i)
        prev_values[n] = i # Записываем само число n как ключ, а его индекс i как значение

print(prev_values)
s = "Yandex"
r = s[: :-1]
print (r) 

s = "Yandex"
result_loop = ""
for char in s:
    result_loop = char + result_loop 
    # Мы приклеиваем букву В НАЧАЛО новой строки
print (result_loop)    


s = "Yandex"
result_method = "".join(reversed(s))
print (result_method)  
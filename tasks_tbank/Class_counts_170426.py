class FrequencyFinder:
    # Конструктор класса создал объект и наполняет нач-данными.
    def __init__(self, data_list):
        self.data = data_list
    # self.data Атрибут объекта - «внутренняя память» объекта.

    # Метод класса. Выполняет основную логику поиска.
    # self — это ссылка на конкретный экземпляр (объект).
    # Она позволяет методам обращаться к его же атрибутам.
    def find_most_frequent(self): 
        counts = {}
        for item in self.data:
            counts[item] = counts.get(item, 0) + 1
    # Итерация по self.data и наполнение словаря — 
    # это формирование гистограммы частот.    
        max_val = max(counts.values())
        
        result = []
        for k, v in counts.items():
            if v == max_val:
                result.append(k)
        return result # в print(finder.find_most_frequent())

# 1. Объявляем экземпляр (объект) класса FrequencyFinder.
# Инстанцирование - создал инстанс (экземпляр, объект) класса.
# Переменная finder теперь хранит ссылку на этот объект.
finder = FrequencyFinder([1, 4, 3, 2, 3, 4, 4, 3, 2])

# 2. Вызываем метод find_most_frequent у объекта finder.
#    Метод анализирует данные внутри объекта и возвращает результат.
#    Функция print выводит этот результат на экран.
print(finder.find_most_frequent());


# Для сравнения - "безклассовое" оформление:
figures = [1, 3, 3, 2, 5, 2, 1, 3, 1]

counts = {}
for figure in figures:
    # Метод .get берет старое значение или 0, и мы прибавляем 1
    counts[figure] = counts.get(figure, 0) + 1

# Метод .values() дает список всех счетчиков: [3, 3, 2, 1]
# Функция max() находит самое большое число в этом списке: 3
max_count = max(counts.values())

result = None
# Метод .items() дает доступ сразу к паре (ключ, значение)
for key, value in counts.items():
    if value == max_count:
        result = key       #  print(key) - печатаем сразу и 1, и 3, то внутри условия
        print (result)     
              
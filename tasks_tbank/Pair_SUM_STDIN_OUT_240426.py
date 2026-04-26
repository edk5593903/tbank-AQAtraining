import sys

def main():
    data = sys.stdin.read().strip().split()
    # data — это список строк, прочитанных из stdin, разделённых пробелами/переводами строки

    # Предположим формат вводимых данных (stdin):
    # первая строка: N
    # вторая строка: N чисел
    # третья строка: target
    #
    # Например:
    # 4
    # 2 7 11 15
    # 9

    n = int(data[0])                 # количество чисел
    nums = list(map(int, data[1:1+n]))
    target = int(data[1+n])

    prev_values = {}

    for i, x in enumerate(nums):
        diff = target - x
        if diff in prev_values:
            # выводим индексы через пробел
            print(prev_values[diff], i)
            return
        else:
            prev_values[x] = i

    # если пары нет — на контесте обычно нужно либо ничего не выводить,
    # либо вывести -1; здесь выберем -1
    print(-1)

if __name__ == "__main__":
    main()
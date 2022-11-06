'''
Последний индекс хипы
Задан массив из
n
n целых чисел. Определите индекс последнего элемента массива, входящего в бинарную кучу для максимума.

Формат ввода
В первой строке входных данных содержится целое число (1≤n≤10 6).

Формат вывода
В единственной строке выходных данных выдайте индекс последнего элемента массива, входящего в кучу. Нумерация с 0.
'''

n = int(input())
if n > 0:
    heap = list(map(int, input().split()))
    res_idx = 0

    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        if (left < n):
            if (heap[i] >= heap[left]):
                res_idx = left
            else:
                break
        if (right < n):
            if (heap[i] >= heap[right]):
                res_idx = right
            else:
                break

    print(res_idx)

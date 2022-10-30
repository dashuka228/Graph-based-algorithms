'''
Полустепени вершин по спискам ребер
Ориентированный граф задан списком ребер. Найдите степени всех вершин графа.

Формат ввода
Сначала вводятся числа n (1 <= n <= 100) – количество вершин в графе и m (1 <= m <= n(n-1)) – количество ребер.
Затем следует m пар чисел – ребра графа.

Формат вывода
Выведите n пар чисел – для каждой вершины сначала выведите полустепень захода и затем полустепень исхода.
'''

n, m = map(int, input().split())
edge_arr = []

for i in range (m):
    edge_arr.append(list(map(int, input().split())))

degrees_arr = []
for i in range(n):
    degrees_arr.append([0] * 2)


for i in range(m):
    degrees_arr[edge_arr[i][1] - 1][0] += 1
    degrees_arr[edge_arr[i][0] - 1][1] += 1

for i in range(n):
    for j in range(2):
        print(degrees_arr[i][j])
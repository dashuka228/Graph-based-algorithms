'''
От матрицы смежности к списку ребер, ориентированный вариант
Ориентированный граф задан матрицей смежности, выведите его представление в виде списка ребер.

Формат ввода
На вход программы поступает число n (1<=n<=100) – количество вершин графа,
а затем n строк по n чисел, каждое из которых равно 0 или 1, – его матрица смежности.

Формат вывода
Выведите список ребер заданного графа.
'''

n = int(input())
add_arr = []
new_arr = []

for i in range(n):
    add_arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if add_arr[i][j] == 1:
            new_arr.append([i + 1, j + 1])

for i in range(len(new_arr)):
    for j in range(len(new_arr[i])):
        print(str(new_arr[i][j]), end=' ')
    print()
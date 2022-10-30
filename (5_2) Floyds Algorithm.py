'''
Флойд
Полный ориентированный взвешенный граф задан матрицей смежности.
Постройте матрицу кратчайших путей между его вершинами. Гарантируется, что в графе нет циклов отрицательного веса.

Формат ввода
В первой строке вводится единственное число N – количество вершин графа.
В следующих N строках по N чисел задается матрица смежности графа.
Все числа по модулю не превышают 100. На главной диагонали матрицы – всегда нули.

Формат вывода
Выведите N строк по N чисел – матрицу кратчайших расстояний между парами вершин.
'''

n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

#https://www.youtube.com/watch?v=oNI0rf2P9gE&ab_channel=AbdulBari
tec = n
for tec in range(n):
    new_graph = graph.copy()
    for i in range(n):
        for j in range(n):
            if i != j:
                new_graph[i][j] = min(new_graph[i][j], new_graph[i][tec] + new_graph[tec][j])

for i in range(n):
    for j in new_graph[i]:
        print(j, end = " ")
    print()
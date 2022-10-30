'''
Алгоритм Дейкстры
Дан ориентированный взвешенный граф. Для него вам необходимо найти кратчайшее расстояние от вершины S до вершины F.

Формат ввода
В первой строке входных данных содержатся три числа: N, S и F
где N – количество вершин графа.
В следующих N строках записаны по N чисел – матрица смежности графа,
где число в i-ой строке и j-ом столбце соответствует ребру из i в j: -1 означает отсутствие ребра между вершинами,
а любое неотрицательное число – наличие ребра данного веса. На главной диагонали матрицы всегда записаны нули.

Формат вывода
Выведите искомое кратчайшее расстояние или -1, если пути между указанными вершинами не существует.
'''
import math

def findTheLighterPick (weight, visited):
    min_weight = max(weight)
    min_pick = -1
    for i in range(len(weight)):
        if visited[i] == False:
            if weight[i] < min_weight:
                min_weight = weight[i]
                min_pick = i
    return min_pick

n, start, finish = map(int, input().split())
start -= 1
finish -= 1
graph = {i:[] for i in range(0, n)}

for i in range(n):
    line = (list(map(int, input().split())))
    for j in range(n):
        if line[j] > 0:
            graph[i].append([j, line[j]])

inf = math.inf
parents = [] * n
visited = [False] * n
weight = [inf] * n
weight[start] = 0
pick = start

#https://www.youtube.com/watch?v=MCfjc_UIP1M&ab_channel=selfedu
while pick != -1:
    visited[pick] = True
    for i in range(len(graph[pick])):
        connected_pick = graph[pick][i][0]
        edge_weight = graph[pick][i][1]
        if visited[connected_pick] == False:
            new_weight = weight[pick] + edge_weight
            if new_weight < weight[connected_pick]:
                weight[connected_pick] = new_weight
    pick = findTheLighterPick(weight, visited)

if weight[finish] == inf:
    print("-1")
else:
    print(weight[finish])
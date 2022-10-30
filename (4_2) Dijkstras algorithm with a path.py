'''
Дейкстра: восстановление пути
Дан ориентированный взвешенный граф. Найдите кратчайший путь от одной заданной вершины до другой.

Формат ввода
В первой строке содержатся три числа: N, S и F
где N – количество вершин графа, S – начальная вершина, а F – конечная.
В следующих N строках вводится по N чисел, не превосходящих 100,
– матрица смежности графа, где −1 означает отсутствие ребра между вершинами,
а любое неотрицательное число – присутствие ребра данного веса.
На главной диагонали матрицы записаны нули.

Формат вывода
Требуется вывести последовательно все вершины одного (любого) из кратчайших путей, или одно число -1,
если пути между указанными вершинами не существует.
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

def findTheWay (parents, start, finish):
    tec_pick = finish
    way = []
    while tec_pick != start:
        way.insert(0, tec_pick + 1)
        tec_pick = parents[tec_pick]
    way.insert(0, start + 1)
    return(way)

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
visited = [False] * n
parents = [-1] * n
weight = [inf] * n
weight[start] = 0
pick = start

while pick != -1:
    visited[pick] = True
    for i in range(len(graph[pick])):
        connected_pick = graph[pick][i][0]
        edge_weight = graph[pick][i][1]
        if visited[connected_pick] == False:
            new_weight = weight[pick] + edge_weight
            if new_weight < weight[connected_pick]:
                weight[connected_pick] = new_weight
                parents[connected_pick] = pick
    pick = findTheLighterPick(weight, visited)

if weight[finish] == inf:
    print("-1")
else:
    way = findTheWay (parents, start, finish)
    for i in way:
        print(i, end = " ")
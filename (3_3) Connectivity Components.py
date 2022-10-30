'''
Компоненты связности
Дан неориентированный невзвешенный граф. Необходимо посчитать количество его компонент связности и вывести их.
Формат ввода
Во входном файле записано два числа N и M (0 < N <= 100000, 0 <= M <= 100000).
В следующих M строках записаны по два числа i и j (1 <= i, j <= N), которые означают, что вершины i и j соединены ребром.
Формат вывода
В первой строчке выходного файла выведите количество компонент связности. Далее выведите Nцелых чисел,
i-е из них задаёт номер компоненты связности для i-й вершины.
Компоненты следует нумеровать последовательными целыми числами от 1. Порядок нумерации компонент произвольный.
'''

import sys
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
graph = {i:[] for i in range(1, n + 1)}

for i in range(m):
    line = (list(map(int, input().split())))
    graph[line[0]].append(line[1])
    graph[line[1]].append(line[0])

color = [0] * n
components = [0] * n
current_component = 0

def dfs (graph, components, pick, current_component):
    components[pick - 1] = current_component
    for i in graph[pick]:
        if components[i - 1] == 0:
            dfs(graph, components, i, current_component)
    return components

for i in range(n):
    if components[i] == 0:
        current_component += 1
        components[i] = current_component
        components = dfs (graph, components, i + 1, current_component)


print(current_component)
for i in components:
    print(i, end = " ")
'''
Вес компоненты
В неориентированный взвешенный граф добавляют ребра.
Напишите программу, которая в некоторые моменты находит сумму весов ребер в компоненте связности.

Формат ввода
В первой строке записано два числа n и m (1≤n,m≤10ˆ6) - количество вершин в графе и количество производимых добавлений и запросов.
Далее следует m строк с описанием добавления или запроса. Каждая строка состоит из двух или четырех чисел.
Первое из чисел обозначает код операции. Если первое число 1, то за ним следует еще три числа x, y, w.
Это означает, что в граф добавляется ребро из вершины x в вершину y веса w. (1≤x<y≤n, 1≤w≤10ˆ3).
Кратные ребра допустимы. Если первое число 2, то за ним следует ровно одно число x.
Это означает, что необходимо ответить на вопрос, какова сумма ребер в компоненте связности, которой принадлежит вершина x (1≤x≤n).

Формат вывода
Для каждой операции с кодом 2 выведите ответ на поставленную задачу. Ответ на каждый запрос выводите на отдельной строке.
'''

def addEdge (v1, v2, w, graph):
    graph[v1].append([v2, w])
    graph[v2].append([v1, w])
    return graph

def addInResult (result, number):
    result.append(number)
    return result

def countWeight (v, graph, n):
    weight = 0
    if len(graph[v]) > 0:
        visited = [False] * n
        queue = []
        queue.append(v)
        while len(queue) > 0:
            temp_v = queue.pop()
            if len(graph[temp_v]) > 0 and visited[temp_v - 1] == False:
                for a, w in graph[temp_v]:
                    if visited[a - 1] == False:
                        visited[temp_v - 1] = True
                        weight += w
                        queue.append(a)
            else:
                continue
    return weight

n, m = map(int, input().split())

operations = []
for i in range(m):
    operations.append(list(map(int, input().split())))

graph = []
graph = {i:[] for i in range(1, n + 1)}
result = []

for i in range (m):
    data = operations[i]
    if operations[i][0] == 1:
        graph = addEdge(data[1], data[2], data[3],  graph)
    else:

        addInResult(result, countWeight(data[1], graph, n))

for i in result:
    print(i)
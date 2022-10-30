'''
Поиск в глубину
Дан неориентированный граф, возможно, с петлями и кратными ребрами.
Необходимо построить компоненту связности, содержащую первую вершину.

Формат ввода
В первой строке записаны два целых числа N (1 ≤ N ≤ 103) и M (0 ≤ M ≤ 5 * 105) — количество вершин и ребер в графе.
В последующих M строках перечислены ребра — пары чисел, определяющие номера вершин, которые соединяют ребра.

Формат вывода
В первую строку выходного файла выведите число K — количество вершин в компоненте связности.
Во вторую строку выведите K целых чисел — вершины компоненты связности, перечисленные в порядке возрастания номеров.
'''

n, m = map(int, input().split())

graph = {i:[] for i in range(n)}
for i in range(m):
    inn, outt = map(int, input().split())
    graph[inn - 1].append(outt - 1)
    graph[outt - 1].append(inn - 1)

result = set()
to_check = set()
to_check.add(0)
l = -1
while len(result)!= l:
    l = len(result)
    new_to_check = set()
    for i in to_check:
        result.add(i)
        for j in graph[i]:
            new_to_check.add(j)
    to_check = new_to_check

print(len(result))
print(*list(map(lambda x: x + 1, result)))
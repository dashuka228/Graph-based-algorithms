'''
Авиаперелеты (Форд-Белман)
Профессору Форду необходимо попасть на международную конференцию.
Он хочет потратить на дорогу наименьшее количество денег, поэтому решил,
что будет путешествовать исключительно ночными авиарейсами (чтобы не тратиться на ночевку в отелях),
а днем будет осматривать достопримечательности тех городов, через которые он будет проезжать транзитом.
Он внимательно изучил расписание авиаперелетов и составил набор подходящих авиарейсов,
выяснив, что перелеты на выбранных направлениях совершаются каждую ночь и за одну ночь он не сможет совершить два перелета.

Теперь профессор хочет найти путь наименьшей стоимости, учитывая что до конференции осталось K ночей
(то есть профессор может совершить не более K перелетов).

Формат ввода
В первой строке находятся числа N (количество городов), M (количество авиарейсов),
K (количество оставшихся ночей), S (номер города, в котором живет профессор), F (номер города, в котором проводится конференция).

Ограничения: 2≤N≤100, 1≤M≤10ˆ5, 1≤K≤100, 1≤S≤N, 1≤F≤N.

Далее идет M строк, задающих расписание авиарейсов. i-я строка содержит три натуральных числа:
Si, Fi и Pi, где Si - номер города,
из которого вылетает i-й рейс, Fi - номер го-рода, в который прилетает i-й рейс, Pi - стоимость перелета i-м рейсом.
 1≤Si≤N, 1≤Fi≤N, 1≤Pi≤10ˆ6.

Формат вывода
Выведите одно число - минимальную стоимость пути, подходящего для профессора.
Если профессор не сможет за K ночей добраться до конференции, выведите число -1.
'''

import math

n, m, k, start, finish = map(int, input().split())

graph = {i:[] for i in range(1, m + 1)}

for i in range(1, m + 1):
    graph[i] = (list(map(int, input().split())))

inf = math.inf
weight = [inf] * (n + 1)
weight[start] = 0

#https://www.youtube.com/watch?v=5eIK3zUdYmE&ab_channel=NeetCode

for i in range(k):
    temp = weight.copy()
    for j in range(1, m + 1):
        source = graph[j][0]
        destination = graph[j][1]
        new_weight = graph[j][2]
        if weight[source] == inf:
            continue
        if weight[source] + new_weight < temp[destination]:
            temp[destination] = weight[source] + new_weight
    weight = temp.copy()



if weight[finish] == inf:
    print("-1")
else:
    print(weight[finish])
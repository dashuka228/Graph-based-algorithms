'''
Хипуй
В этой задаче вам необходимо организовать структуру данных Heap для хранения целых чисел,
над которой определены следующие операции:
a) Insert(k) – добавить в Heap число k (1 ≤ k ≤ 1000000) ;
b) Extract достать из Heap наибольшее число (удалив его при этом).

Формат ввода
В первой строке содержится количество команд N (1 ≤ N ≤ 100000),
далее следуют N команд, каждая в своей строке.
Команда может иметь формат: “0 <число>” или “1”,
обозначающий, соответственно, операции Insert(<число>) и Extract.
Гарантируется, что при выполенении команды Extract в структуре находится по крайней мере один элемент.

Формат вывода
Для каждой команды извлечения необходимо отдельной строкой вывести число, полученное при выполнении команды Extract.
'''

import sys
sys.setrecursionlimit(1100000)

def heaplify (heap, i, n):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if (left < n) and (heap[left] > heap[largest]):
        largest = left
    if (right < n) and (heap[right] > heap[largest]):
        largest = right

    if largest == i:
        return i
    else:
        heap[largest], heap[i] = heap[i], heap[largest]
        heaplify(heap, largest, n)

def insertIntoHeap (value, heap):
    heap.append(value)
    i = len(heap) - 1
    parent = (i - 1) // 2
    while (i > 0) and (heap[parent] < heap[i]):
        heap[i], heap[parent] = heap[parent], heap[i]
        i = parent
        parent = (i - 1) // 2

def extractFromHeap (heap):
    new_result = heap.pop(0)
    if len(heap) > 2:
        heap.insert(0, heap.pop(-1))
        heaplify(heap, 0, len(heap))
    else:
        if len(heap) == 2:
            if heap[1] > heap[0]:
                heap[0], heap[1] = heap[1], heap[0]
    return new_result

m = int(input())
operations = []
heap = []
result = []
for i in range(m):
    operations.append(list(map(int, input().split())))

for i in range(m):
    current_operation = operations[i]
    if current_operation[0] == 0:
        insertIntoHeap (current_operation[1], heap)
    else:
        result.append(extractFromHeap(heap))

for i in result:
    print(i)
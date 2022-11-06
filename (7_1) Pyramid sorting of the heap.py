'''
Пирамидальная сортировка
Вам необходимо реализовать пирамидальную сортировку.

Формат ввода
В первой строке - одно целое число n (0≤n≤10) – количество чисел, которые надо отсортировать.

Во второй строке записано
n целых чисел

Формат вывода
Выведите отсортированный массив через пробел.

'''

import sys
sys.setrecursionlimit(1100000)

#https://www.youtube.com/watch?v=e4gv3pnHWy0&ab_channel=Plyas_IT

def heaplify (heap, i, n):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if (left <= n) and (heap[left] > heap[largest]):
        largest = left
    if (right <= n) and (heap[right] > heap[largest]):
        largest = right

    if largest == i:
        return i
    else:
        heap[largest], heap[i] = heap[i], heap[largest]
        heaplify(heap, largest, n)

def buildHeap (heap):
    middle = len(heap) // 2
    for i in range (middle, -1, -1):
        heaplify(heap, i, len(heap) - 1)


def sortHeap (heap):
    buildHeap(heap)
    for j in range (len(heap) - 1, -1, -1):
        heap[0], heap[j] = heap[j], heap[0]
        heaplify(heap, 0, j - 1)


n = int(input())
if n > 0:
    heap = list(map(int, input().split()))
    sortHeap(heap)
    for i in heap:
        print(i, end = " ")

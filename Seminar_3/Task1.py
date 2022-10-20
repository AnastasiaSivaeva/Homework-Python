#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции

import random

N = int(input('Введите количество элементов: '))

def ListOfElem(n):
    el = random.randint(-n, n)
    return el

list = []
for i in range(N):
    list.append(ListOfElem(N))

def SumOfElem(arr):
    sum = 0
    for i in range(len(list)):
        if i % 2 != 0:
           sum += arr[i]
    return sum

print(f'Список из {N} элементов: {list} ')
print(f'Сумма элементов: {format(SumOfElem(list))} ')
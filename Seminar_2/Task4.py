#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры

from random import random


N = int(input('Введите количество элементов: '))
M = input('Введите позиции элементов через пробел: ').split()

import random

def ListOfElem(n):
    el = random.randint(-n, n)
    return el

list = []
for i in range(N):
    list.append(ListOfElem(N))

def ProdOfElem(m, arr):
    prod = 1
    for m in arr:
        prod = prod * m
    return prod




print(f'Список из {N} элементов: {list} ')
print(f'Произведение элементов: {format(ProdOfElem(M, list))} ')

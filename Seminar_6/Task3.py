#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции

import random


amountOfEl = int(input('Введите количество элементов: '))

lst = [random.randint(-amountOfEl, amountOfEl) for i in range(1, amountOfEl + 1)]

lst2 = [lst[i] for i in list(filter(lambda x:  x % 2 != 0, range(len(lst))))]
print(lst)
print(lst2)
print(sum(lst2))


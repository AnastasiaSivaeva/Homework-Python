#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов

import random

num = int(input('Введите количество элементов: '))


lst = [random.uniform(0, 5) for i in range(1, num + 1)]

New_list = [round(i % 1, 2) for i in lst if i % 1 != 0]
print(lst)
print(New_list)
print(max(New_list) - min(New_list))

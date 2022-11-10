 #Реализуйте алгоритм перемешивания списка

import random

N = int(input('Введите количество элементов: '))

def ListOfElem(n):
    el = random.randint(-n, n)
    return el

list = []
for i in range(N):
    list.append(ListOfElem(N))

def SuffleList(list):
    new_list = [] 
    for i in range(len(list)):
        pos = random.randint(0, len(list) - 1)
        new_list.append(list[pos])
        del list[pos]
    list = new_list
    return list

print(f'Список из {N} элементов: {list} ')
print(f'Перемешанный список: {format(SuffleList(list))} ')
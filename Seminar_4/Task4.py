#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
#многочлена и записать в файл многочлен степени k
#k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
#Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени

k = int(input("Введите натуральную степень k: "))

import random


def RandomNum():
    return random.randint(0,101)

def create_mn(k):
    list = [RandomNum() for i in range(k+1)]
    return list



print(create_mn(k))


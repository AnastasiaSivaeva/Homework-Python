#Напишите программу, которая будет преобразовывать десятичное число в двоичное

from ast import Num


num = int(input("Введите десятичное число для преобразовывания его в двоичное: "))


def Number(N):
   Num = ""
   while N != 0:
    Num = str(N % 2) + Num
    N = N // 2
   return Num


print(f'Получившееся число: {format(Number(num))} ')

#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N
import math
from re import I


num = int(input("Введите число: "))

def NumMult(number):
    list = []
    i = 2
    while i <= number:
        if number % i == 0:
           list.append(i)
           number //= i
           i = 2
        else:
            i += 1
    return list

print(f'список простых множителей числа {num}: {format(NumMult(num))} ')




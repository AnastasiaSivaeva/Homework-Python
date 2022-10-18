#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

def ProdOfNum(num):
    res = 0
    if num == 1:
         return 1
    else:
         res = num * ProdOfNum(num - 1)
    return res

number = int(input('Введите число: '))

list = []
for i in range(1, number + 1):
    list.append(ProdOfNum(i))



print(f'Набор произведений чисел от 1 до {number} : {list} ')
#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

number = int(input('Введите число: '))

def ProdOfNum(x):
    prod = 1
    for i in x:
        prod *= i
    return prod


lst = list(map(lambda x: ProdOfNum(list(range(1,x+1))), range(1, number + 1))) 
print(f"Итоговый набор {lst}")
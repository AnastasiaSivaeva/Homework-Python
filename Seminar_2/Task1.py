#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр

def SumNumber(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i) 
    return sum


number = float(input('Введите число: '))

print(f"Сумма цифр = {format(SumNumber(number))}")

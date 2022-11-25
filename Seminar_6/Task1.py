#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр

number = float(input('Введите число: '))

new_list = list(str(number).split('.'))

sum = sum(map(int, str(number).replace('.', '')))

print(f'{sum}')
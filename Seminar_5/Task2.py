#Создайте программу для игры с конфетами человек против человека.

from random import randint

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
amount = 221

import random

lot = random.randint(0,2) 
if lot == 1:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")


def input_dat(player):
    x = int(input(f"{player}, введите количество конфет от 1 до 28: "))
    if x < 1 or x > 28:
        x = int(input(f"{player}, введите корректное количество конфет: "))
    return x


count1 = 0
count2 = 0
candies1 = 0 
candies2 = 0
while amount > 0:
    if lot:
        k = input_dat(player1)
        candies1 += k
        amount -= k
        count1 += 1
        lot = False
        print(f"На столе осталось {amount} конфет.")
    else:
        k = input_dat(player2)
        candies2 += k
        amount -= k
        count2 += 1
        lot = True
        print(f"На столе осталось {amount} конфет.")
if count1 > count2:
    print(f"Выиграл {player1}, он взял {candies1} конфет")
else:
    print(f"Выиграл {player2}, он взял {candies2} конфет")


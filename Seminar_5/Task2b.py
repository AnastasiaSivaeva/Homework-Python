#б) Подумайте, как наделить бота "интеллектом"

from random import randint

player1 = input("Введите имя первого игрока: ")
player2 = "Bot"
amount = 221

import random

lot = random.randint(0,2) 
if lot == 1:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")


def input_dat(player1):
    x = int(input(f"{player1}, введите количество конфет от 1 до 28: "))
    if x < 1 or x > 28:
        x = int(input(f"{player1}, введите корректное количество конфет: "))
    return x

def bot(amount):
    k = random.randint(1,28)
    if amount == 28:
        k = 28
    elif amount - k < 28 or amount - k == 28:
        k = random.randint(1,28)
    return k

count1 = 0
count2 = 0
candies1 = 0 
candies2 = 0
while amount > 0:
    if lot == 1:
        k = input_dat(player1)
        if k < amount or k == amount:
            candies1 += k
            amount -= k
            count1 += 1
            lot = False
            print(f"На столе осталось {amount} конфет.")
        else:
            print(f"{player1}, количество конфет не должно превышать {amount}.")

    else:
        k = bot(amount) 
        if k < amount or k == amount:
            candies2 += k
            amount -= k
            count2 += 1
            lot = True
            print(f"Игрок {player2} выбрал {k} количество конфет, на столе осталось {amount} конфет.")
        else:
            k = bot(amount)
            candies2 += k
            amount -= k
            count2 += 1
            lot = True
            print(f"Игрок {player2} выбрал {k} количество конфет, на столе осталось {amount} конфет.")
if count1 > count2:
    print(f"Выиграл {player1}, он взял {candies1} конфет")
else:
    print(f"Выиграл {player2}, он взял {candies2} конфет")

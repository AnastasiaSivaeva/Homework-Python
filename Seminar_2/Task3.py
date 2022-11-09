#Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму

n = int(input('Введите число: '))

def ListOfNumbers(num):
    res = round((1 + 1 / num) ** num, 2)
    return res

list = []
for i in range(1, n + 1):
    list.append(ListOfNumbers(i))


print(f'Список чисел {list}, Сумма: {round(sum(list),2)}')
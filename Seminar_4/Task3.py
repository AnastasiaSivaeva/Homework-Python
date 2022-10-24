#Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
#исходной последовательности

list2 = list(map(int, input("Введите числа без пробела:").split()))

def NewListOfNumbers(list2):
    new_list = []
    for num in list2:
        if num not in new_list :
            new_list.append(num)
    return new_list

print(f"Исходный список: {list2}")
print(f'Список из неповторяющихся элементов: {format(NewListOfNumbers(list2))} ')


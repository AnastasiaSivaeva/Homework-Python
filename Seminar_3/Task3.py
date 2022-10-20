#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов


#List = list(map(float, input("Введите числа через пробел:").split()))

#for i in List:
#    if i % 1 != 0:
#        New_list = [round(i % 1, 2)]
#print(max(New_list) - min(New_list))


List = list(map(float, input("Введите числа через пробел:").split()))
New_list = [round(i % 1, 2) for i in List if i % 1 != 0]
print(max(New_list) - min(New_list))
#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)

quarter = int(input('Введите номер четверти плоскости: '))

if int(quarter) != 1 and int(quarter) != 2 and int(quarter) != 3 and int(quarter) != 4:
    print('Введите корректное значение номера четверти плоскости')
else:
     if int(quarter) == 1:
         print('Значение координаты x- позитивная бесконечность, значение координаты y- позитивная бесконечность')
     elif int(quarter) == 2:
         print('Значение координаты x- отрицательная бесконечность, значение координаты y- позитивная бесконечность')
     elif int(quarter) == 3:
         print('Значение координаты x- отрицательная бесконечность, значение координаты y- отрицательная бесконечность')
     elif int(quarter) == 4:
         print('Значение координаты x- позитивная бесконечность, значение координаты y- отрицательная бесконечность')


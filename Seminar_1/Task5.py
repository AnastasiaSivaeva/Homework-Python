#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве

xy1 = input('Введите координаты X и Y первой точки через пробел: ').split()
xy2 = input('Введите координаты X и Y второй точки через пробел: ').split()

distance = ((int(xy2[0]) - int(xy1[0])) ** 2 + (int(xy2[1]) - int(xy1[1])) ** 2) ** 0.5

print(f'Расстояние между точками равно {format(distance, ".2f")}')
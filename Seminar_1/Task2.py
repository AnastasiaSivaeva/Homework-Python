#Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

xyz = input('Введите значение X Y Z через пробел: ').split()

left = not(int(xyz[0]) or int(xyz[1]) or int(xyz[2]))
right = not int(xyz[0]) and not int(xyz[1]) and not int(xyz[2])

if left == right:
    print('Утверждение верно')
else:
    print('Утверждение ложно')
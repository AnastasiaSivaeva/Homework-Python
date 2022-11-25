#Вычислить число Пи c заданной точностью d


d =  input("Введите число для заданной точности числа Пи: ").split()

pi = 0
for i in range(1, 100) : pi = pi+4*((-1)**(i+1))/(2*i-1)
#print(round(pi, len(d)))


print(round(pi, 2))



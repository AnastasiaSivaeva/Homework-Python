#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д


List = list(map(int,input('Введите числа через пробел:').split()))


#def ProdOfElem(List):
 #   new_list = []
  #  if len(List) % 2 != 0:
  #      l = len(List) // 2 + 1 
  #  else:
  #      l = len(List) // 2
  #  for i in range(l):
  #      new_list = [List[i] * List[len(List) - i - 1]]
  #  return new_list


#print(f'Список элементов: {List} ')
#print(f'Произведение пар чисел: {format(ProdOfElem(List))} ')


l = len(List) // 2 + 1 if len(List) % 2 != 0 else len(List) // 2
New_list = [List[i] * List[len(List) - i - 1] for i in range(l)]
print(New_list)
#Напишите программу, удаляющую из текста все слова, содержащие ""абв""

text = input("Введите слова через пробел:")
print(f"Исходный текст: {text}")

def FindWords(text):
    find = "абв"
    list = []
    for i in text.split():
        if find not in i:
            list = [i]
    return " ".join(list)

print(f'Результат: {format(FindWords(text))}')
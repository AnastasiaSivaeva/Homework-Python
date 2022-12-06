def view_data(data):
    return data

def choice():
    selector = None
    selector = int(input('Введите "1" если хотите найти контакт\n' + \
                        'Введите "2" если хотите добавить новый контакт\n' + \
                        'Введите "3" если хотите удалить контакт\n' + \
                        'Введите "4" если хотите просмотреть всю адресную книгу\n' + \
                        ': '))
    if selector > 4:
        print('Не корректный ввод!!!\n')
        print('Необходимо ввести целое число!!!\n')
    return selector

while True:
    selector = choice()
    if selector == 1:
        query = ((input('Для поиска контакта введите его фамилию: ').capitalize(),
                  input('Для поиска контакта введите его имя: ').capitalize()))
        print(findCont(query))
    elif selector == 2:
        addCont()
    elif selector == 4:
        showAllContacts()
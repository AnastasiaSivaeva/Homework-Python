import data_provider
import logger

print('\nВас приветствует телефонная книга')


def menu():
    while True:
        print('\nМЕНЮ')
        print('1. Показать все записи.')
        print('2. Найти номер по фамилии.')
        print('3. Найти номер по имени.')
        print('4. Поиск по номеру телефона.')
        print('5. Добавить новую запись.')
        print('6. Изменить существующую запись.')
        print('7. Удалить запись.')
        print('8. Закрыть программу.\n')
        n = (input('Выберите пункт меню: '))

        if n == 1:
           logger.log(n)
           print(data_provider.showAllContacts())
        
        elif n == 2:
            logger.log(n)
            search = input('Введите фамилию: ')
            logger.log(search)
            print(data_provider.showAllContacts(surname=search))

        elif n == 3:
            logger.log(n)
            search = input('Введите имя: ')
            logger.log(search)
            print(data_provider.showAllContacts(name=search))

        elif n == 4:
            logger.log(n)
            search = input('Введите номер  телефона: ')
            logger.log(search)
            print(data_provider.showAllContacts(number=search))

        elif n == 5:
            logger.log(n)
            name = input('Введите имя: ')
            logger.log(name)
            surname = input('Введите фамилию: ')
            logger.log(surname)
            number = input('Введите номер телефона: ')
            logger.log(number)
            data_provider.create(name, surname, number)

        elif n == 6:
            logger.log(n)
            print('1. Найти номер по фамилии.')
            print('2. Найти номер по имени.')
            print('3. Поиск по номеру телефона.')
            change = (input('Введите номер пункта: '))

            if change == 1:
                logger.log(change)
                search = input('Введите фамилию: ')
                logger.log(search)
                data_provider.showAllContacts(surname=search)
                new_number = input('Введите новый номер телефона: ')
                logger.log(new_number)
                data_provider.update(new_number=new_number)

            elif change == 2:
                logger.log(change)
                search = input('Введите имя: ')
                logger.log(search)
                data_provider.showAllContacts(name=search)
                new_number = input('Введите новый номер телефона: ')
                logger.log(new_number)
                data_provider.update(new_number=new_number)

            elif change == 3:
                logger.log(change)
                search = input('Введите номер телефона: ')
                logger.log(search)
                data_provider.showAllContacts(number=search)
                new_number = input('Введите новый номер телефона: ')
                logger.log(new_number)
                data_provider.update(new_number=new_number)

            else:
                print(
                    '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')
                
        elif n == 7:
            logger.log(n)
            print('1. Найти номер по фамилии.')
            print('2. Найти номер по имени.')
            print('3. Поиск по номеру телефона.')
            deleting = (input('Введите номер пункта: '))

            if deleting == 1:
                logger.log(deleting)
                search = input('Введите фамилию: ')
                logger.log(search)
                print(data_provider.showAllContacts(surname=search))
                user_id = input('Введите id записи: ')
                logger.log(user_id)
                data_provider.delete(id=user_id)

            elif deleting == 2:
                logger.log(deleting)
                search = input('Введите имя: ')
                logger.log(search)
                print(data_provider.showAllContacts(name=search))
                user_id = input('Введите id записи: ')
                logger.log(user_id)
                data_provider.delete(id=user_id)

            elif deleting == 3:
                logger.log(deleting)
                search = input('Введите номер телефона: ')
                logger.log(search)
                print(data_provider.showAllContacts(number=search))
                user_id = input('Введите id записи: ')
                logger.log(user_id)
                data_provider.delete(id=user_id)

            else:
                print(
                    '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

        elif n == 8:
            logger.log(n)
            print('Спасибо за работу!')
            break


def сheck(arg):
    while arg.isdigit() != True:
        print('\nВы ввели не число.')
        arg = input('Введите соответствующий пункт меню: ')
    return int(arg)
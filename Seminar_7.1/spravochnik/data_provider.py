import csv
import os.path

spravochnik = []
spravochnik_file_name = ''
global_id = 0

def init(file_name = 'spravochnik.csv'):
    global global_id
    global spravochnik
    global spravochnik_file_name
    spravochnik_file_name = file_name
    spravochnik.clear()
    if os.path.exists(spravochnik_file_name):
        with open(spravochnik_file_name, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if(row[0] != 'ID'):
                    spravochnik.append(row)
                    if(int(row[0]) > global_id):
                        global_id = int(row[0])
    else:
        open(spravochnik_file_name, 'w', newline='').close()

def create(name='', surname='', number=''):
    global global_id
    global spravochnik
    global spravochnik_file_name
    if(name == ''):
        print("Имя не указано!")
        return
    if(surname == ''):
        print("Фамилия не указана!")
        return
    if(number == ''):
        print("Телефон не указан!")
        return

    for row in spravochnik:
        if(row[1] == name.title() and row[2] == surname.title() and row[3] == number):
            print("Контакт уже существует")
            return

    global_id += 1
    new_row = [str(global_id), name.title(),
               surname.title(), number]
    spravochnik.append(new_row)
    with open(spravochnik_file_name, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(new_row)

def showAllContacts(id='', name='', surname='', number=''):
    global global_id
    global spravochnik
    global spravochnik_file_name
    result = []
    for row in spravochnik:
        if (id != '' and row[0] != id):
            continue
        if(name != '' and row[1] != name.title()):
            continue
        if(surname != '' and row[2] != surname.title()):
            continue
        if(number != '' and row[3] != number):
            continue
        result.append(row)
    if len(result) == 0:
        return f'Контакты не найдены'
    else:
        return result

def update(id='', new_name='', new_surname='', new_number=''):
    global global_id
    global spravochnik
    global spravochnik_file_name
    with open(spravochnik_file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for row in spravochnik:
            if(row[0] == id):
                if(new_name != ''):
                    row[1] = new_name.title()

                if(new_surname != ''):
                    row[2] = new_surname.title()

                if(new_number != ''):
                    row[3] = new_number

            writer.writerow(row)

def delete(id=''):
    global global_id
    global spravochnik
    global spravochnik_file_name
    if(id == ''):
        print('Контакт удален')
        return

    for row in spravochnik:
        if (row[0] == id):
            spravochnik.remove(row)
            break

    with open(spravochnik_file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for row in spravochnik:
            writer.writerow(row)
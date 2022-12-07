import csv

name = None 
lastName = None 
phoneNumber = None

def init(name, lastName, phoneNumber):
    self.name = name
    self.lastName = lastName
    self.phoneNumber = phoneNumber

def str(self):
        return 'Member({} {} {})'.format(self.lastName, self.name, self.phoneNumber)

def findCont(self, query = None):
        with open('spravochnik.csv') as file:
            if (lastName, name) == query:
                return 'Member({} {} {})'.format(self.lastName, self.name, self.phoneNumber)

def addCont(self):
    if findCont(query=(lastName, name)) is None:
        n = newCont()
        n.inputСharacters()
        f = open('spravochnik.csv', 'a')
        f.write('{} {} {}'.format(n.lastName, n.name, n.phoneNumber))
        print('Контакт {lastName} {name} добавлен в справочник'.format(lastName=n.lastName, name=n.name))
        f.close()
    else:
        print('Такой контакт уже есть')

def showAllContacts(self):
        with open('spravochnik.csv') as file:
            print(member)

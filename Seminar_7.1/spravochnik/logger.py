import user_interface

def log():
    with open('log.csv', 'a') as file:
        file.write('{}'
                    .format(user_interface.menu))


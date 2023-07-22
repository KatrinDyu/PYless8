def print_info(temp):
    print(*temp)


def add_person(data):
    fio = input('введите фамилию и имя латинскими буквами: ')
    tlf = input('введите телефон: ')
    data.append((fio, tlf))
    return data

def delete(data):
    fio = input('фамилия и имя удаляемого: ')
    new_data = []
    for name in data:
        if name[0] != fio:
            new_data.append(name)
    return new_data

def find(data):
    elem = input('я ищу: ')
    finding = []
    for name in data:
        for smth in name:
            if (elem in smth) and name not in finding:
                finding.append(name)
        if finding:
            print(*finding)
        else :
            print('таких нет')


def read_file():
    with open('my_file.txt', 'r') as file:
        temp = file.readlines()
    return temp

def write_file():
    pass

def menu():
    data = read_file()
    while True:
        print('Выберите действие: ')
        print('1 - вывести инфо на экран')
        print('0 - выход из программы')
        print('2 - добавить абонента')
        print('3 - удалить абонента')
        print('4 - искать  абонента')
        n = int(input('ваш выбор: '))
        if n == 0:
            break
        elif n == 1:
            print_info(data)
        elif n == 2:
            add_person(data)
        elif n == 3:
            delete(data)
        elif n == 4:
            find(data)

if __name__ == '__main__':
    menu()

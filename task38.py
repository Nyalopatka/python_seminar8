def menu():
    print("1.Добавить")
    print("2.Вывести всех")
    print("3./Поиск/")
    print("4.стереть все контакты")
    print("5.Выход")
    userInput = int(input('введите номер операции: '))
    if userInput == 1:
        addData()
        return True
    elif userInput == 2:
        printAll()
        return True
    elif userInput == 3:
        find(input("введите имя/фамилию/номер: "))
        return True
    elif userInput == 4:
        clearAll()
        return True
    else:
        return False

def addData():
    with open('file.txt', 'a') as data:
        print('\n'*10) 
        first_name = input("Введите имя: ")
        second_name = input("Введите фамилию: ")
        number = input("Введите номер телефона: ")
        item = [first_name, second_name, number]
        s = ' '
        data.writelines(s.join(item)+'\n')
        print('\n'*10)

def printAll():
    print('\n'*10)
    with open('file.txt', 'r') as data:
        for line in data:
            print(line)
        print('\n')


def find(text):
    print('\n'*10)
    with open('file.txt', 'r') as data:
        for line in data:
            list1 = list(line.strip('\n').split(' '))
        
            if text in list1:
                print(line)
                return line
        print("Не найден!")
        print('\n')
        return


def clearAll():
    with open('file.txt','w') as data:
        print("вы точно хотите стереть все контакты?  yes/no")
        if input(": ") == "yes":
            data.write('')
            print('\n'*10)
            print('*список контактов пуст*')
        else:
            print('\n'*10)
            return True


        
flag = True
while (flag):
   flag = menu()

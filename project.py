import os
import local as lc

path = os.getcwd()

def main():
    while True:
        print(os.getcwd())
        print('1. Просмотр каталога \n'
              '2. На уровень вверх \n'
              '3. На уровень вниз \n'
              '4. Количество файлов и каталогов \n'
              '5. Размер текущего каталога \n'
              '6. Поиск файла \n'
              '7. Выход из программы \n'
              'Выберите пункт меню:')
        command = acceptCommand()
        runCommand((command))
        if command == 7:
            print('Работа программы завершена.')
            break



def acceptCommand():
    command = int(input())
    if  0 < command > 7:
        print('Такой команды не существует.')
    else:
        runCommand(command)



def moveUp():  # Киррил
    b = os.getcwd()
    b = b[::-1]
    for i in b:
        if i == "\\":
            b = b[1:len(b) + 1]
            break
        b = b[1:len(b) + 1]
    b = b[::-1]
    os.chdir(b)
    return local.currdir + os.getcwd()


def runCommand(command):  # Vova
    if command == 1:
        print(os.listdir(os.getcwd()))
    if command == 2:
        moveUp()
    if command == 3:
        moveDown()
    if command == 4:
        countFiles()
    if command == 5:
        countBytes()
    if command == 6:
        print('К сожалению, данная функция пока недоступна.')
    if command == 7:
        print('Работа программы завершена.')
        exit()


def moveDown(currentDir):  # Kirill
    if len(os.listdir(currentDir)) == 0:
        print("ERROR")
    if len(os.listdir(currentDir)) == 1:
        b = os.listdir(currentDir)
        os.chdir(currentDir + "\\" + b[0])
    return local.currdir + os.getcwd()

def countFiles():
    path_f = []
    path = os.getcwd()
    for d, dirs, files in os.walk(path):
        for f in files:
            path = os.path.join(d, f)  # формирование адреса
            path_f.append(path)  # добавление адреса в список
    def countFiles_1(path_f):
        if len(path_f) == 1:
            return 1
        return 1 + countFiles_1(path_f.pop())
    countFiles_1(path_f)


def countBytes():  # Sashka
    pass


def findFiles(): # (TOP TASK) Sashka
    pass

main()

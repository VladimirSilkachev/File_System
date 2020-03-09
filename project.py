# Case-Project
# Силкачев 35% Попов 38% Винников 40%
import os
import local as lc

path = os.getcwd()

def main():
    while True:
        print(os.getcwd())
        print(lc.menu)
        command = acceptCommand()
        runCommand((command))
        if command == 7:
            print(lc.end)
            break



def acceptCommand():
    command = int(input())
    if  0 < command > 7:
        print(lc.not_real)
    else:
        runCommand(command)



def moveUp():  
    b = os.getcwd()
    b = b[::-1]
    for i in b:
        if i == "\\":
            b = b[1:len(b) + 1]
            break
        b = b[1:len(b) + 1]
    b = b[::-1]
    os.chdir(b)
    print(lc.currdir + os.getcwd())


def runCommand(command):  
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
        print(lc.sorry)
    if command == 7:
        print(lc.end)
        exit()


def moveDown(currentDir): 
    if len(os.listdir(os.getcwd())) == 0:
        print (lc.Err)
    if currentDir not in os.listdir(os.getcwd()):
        print(lc.here_no)
    if currentDir in os.listdir(os.getcwd()):
        os.chdir(os.getcwd() + "\\" + currentDir)
        print(lc.currdir + os.getcwd())

def countFiles():
    path_f = []
    path = os.getcwd()
    for d, dirs, files in os.walk(path):
        for f in files:
            path = os.path.join(d, f)       # формирование адреса
            path_f.append(path)             # добавление адреса в список
    def countFiles_1(path_f):
        if len(path_f) == 1:
            return 1
        return 1 + int(countFiles_1(list(path_f.pop())))
    print(lc.count + countFiles_1(path_f))


main()

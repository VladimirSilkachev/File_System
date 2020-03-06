import os
import local as lc

command = input()


def main():
    pass


def acceptCommand():  # vova
    pass


def moveUp():  # Киррил
    pass


def runCommand(command):  # Vova
    pass


def moveDown(currentDir):  # Kirill
    pass


def countFiles(path):  
    path_f = []
    for d, dirs, files in os.walk(path):
        for f in files:
            path = os.path.join(d, f)  # формирование адреса
            path_f.append(path)  # добавление адреса в список
    def countFiles_1(path_f):
        if len(path_f) == 1:
            return 1
        return 1 + countFiles_1(path_f.pop())
    countFiles_1(path_f)


def countBytes(path):  # Sashka
    pass


def findFiles(target, path): # (TOP TASK) Sashka
    pass

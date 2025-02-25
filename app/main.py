from curses import newpad
import os
import sys
from tabnanny import check

d = {
    "exit": "builtin",
    "echo": "builtin",
    "type": "builtin",
    "pwd": "builtin"
}

pwd = os.curdir


def checkPath(path, arg):
    directories = str(path).split(":")
    #print(directories, "all directories")
    for dirs in directories:
        if os.path.exists(dirs):
            listTest = os.listdir(dirs)
        # print(dirs, listTest)
        for file in listTest:
            # print(file, "file is in ", dirs)
            if file == arg:
                return dirs
    return "invalid"


def checkValidCommand(path, command):
    command = str(command).split(" ", 1)
    # print(command[0], d.values())
    if command[0] in d.keys() and len(command) == 2:
        return True, command[0], command[1]
    elif command[0] in d.keys() and len(command) == 1:
        return True, command[0], None
    elif len(command) == 2 and checkPath(path, command[0]) != "invalid":
        return True, command[0], command[1]
    else:
        return False, command[0], None


def main():
    path = os.environ['PATH']
    exit = False

    while True:
        sys.stdout.write("$ ")
        command = input()
        isValid, command, arg = checkValidCommand(path, command)
        if not isValid:
            print(f"{command}: command not found")
        else:
            newPath = checkPath(path, command)
            if newPath != "invalid": 
                #print(command, "in path ", path)
                pwd = newPath
                os.system(command + " " + arg)
            elif command == "pwd":
                print(pwd)
            elif command == "exit":
                sys.exit(int(arg))
            elif command == "echo":
                sys.stdout.write(arg + "\n")
            elif command == "type":
                newPath = checkPath(path, arg)
                pwd = newPath
                if arg in d.keys():
                    print(f"{arg} is a shell {d.get(arg)}")
                elif not newPath == "invalid":
                    print(f"{arg} is {newPath}/{arg}")
                else:
                    print(f"{arg}: not found")


if __name__ == "__main__":
    main()

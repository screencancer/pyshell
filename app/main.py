import os
import sys
import shutil

d = {
    "exit": "builtin" ,
    "echo": "builtin",
    "type": "builtin"
}

def checkPath(path):
    directories = str(path).split(":")
    print(directories, "all directories")
    for dirs in directories:
        if os.path.exists(dirs):
            listTest = os.listdir(dirs)
        #print(dirs, listTest)
        for file in listTest:
            print(file, "file is ")
            if file in d.keys():
                return dirs
    return "invalid"
def checkValidCommand(command):
    command = str(command).split(" ", 1)
    #print(command)
    #print(command[0], d.values())
    if command[0] in d.keys():
        return True, command[0], command[1]
    else:
        return False, command[0], None

def main():
    path = os.environ['PATH']
    #print("Path is " , path)
    exit = False
    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        command = input()
        isValid, command, arg = checkValidCommand(command)
        if not isValid:
            print(f"{command}: command not found")
        else:
            if command == "exit":
                sys.exit(int(arg))
            if command == "echo":
                sys.stdout.write(arg + "\n")
            if command == "type":
                if arg in d.keys():
                    print(f"{arg} is a shell {d.get(arg)}")
                elif not checkPath(path) == "invalid":
                    print(f"{arg} is {path}/{arg}")
                else: 
                    print(f"{arg}: not found")
if __name__ == "__main__":
    main()

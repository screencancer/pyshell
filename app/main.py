import os
import sys

#Dictionary of builtin applications to the program
d = {
    "exit": "builtin",
    "echo": "builtin",
    "type": "builtin",
    "pwd": "builtin",
    "cd": "builtin",
    "cat": "builtin"
}

#Check PATH directory for executables if the exe is not in any path it will return invalid.
def checkPath(path, arg):
    directories = str(path).split(":")
    print(f"checking for{arg} in {path}")
    #Is path right?
    #print(directories, "all directories")
    for dirs in directories:
        if os.path.exists(dirs):
            listTest = os.listdir(dirs)
        #print(dirs, listTest)
        for file in listTest:
            #print(file, "file is in ", dirs)
            if file == arg:
                return dirs
    return "invalid"

def quotationHandler(command: str):
    operand = command[0]
    firstInstanceIndex = command.find(operand)
    secondInstanceIndex = command.find(operand, firstInstanceIndex + 1)
    #print(firstInstanceIndex, secondInstanceIndex)
    arg = command[secondInstanceIndex + 1:len(command)]
    arg = arg.strip()
    command = command[firstInstanceIndex:secondInstanceIndex+1]
    commandList = [command, arg]
    return commandList

#Check if the command given is invalid
def checkValidCommand(path, command: str):
    commandIsQuoted = False
    if command.startswith('"') or command.startswith("'"):
        command = quotationHandler(command)
        #print(command[0])
        #print(command[1])  
    else:
        command = str(command).split(" ", 1) #maybe split it into quote and then split the space AFTER? 
    # print(command[0], d.values())
    # Check if command is in builtin dictionary or checkPath doesnt return invalid meaning it is on PATH
    if command[0] in d.keys() and len(command) == 2:
        return True, command[0], command[1]
    elif command[0] in d.keys() and len(command) == 1:
        return True, command[0], None
    elif len(command) == 2 and checkPath(path, command[0]) != "invalid":
        return True, command[0], command[1]
    elif len(command) == 1 and checkPath(path, command[0]) != "invalid":
        return True, command[0], None
    else:
        return False, command[0], None

#Check if path is valid if so then cd should work
def checkIfValidDirectory(arg):
    try:
        if arg != "~":
            os.chdir(arg)
        else: 
            os.chdir(os.environ['HOME'])
    except:
        print(f"cd: {arg}: No such file or directory")

def main():
    path = os.environ['PATH']
    exit = False

    while True:
        pwd = os.getcwd()
        sys.stdout.write("$ ")
        command = input()
        isValid, command, arg = checkValidCommand(path, command)
        if not isValid:
            print(f"{command}: command not found")
        else:
            newPath = checkPath(path, command)
            #potentially make this a function?
            if newPath != "invalid" and arg != None: 
                #print(command, "in path ", path)
                #pwd = newPath
                os.system(command + " " + arg)
            elif command == "pwd":
                print(pwd)
            elif command == "cd":
                checkIfValidDirectory(arg)
            elif command == "exit":
                sys.exit(int(arg))
            elif command == "echo":
                sys.stdout.write(arg + "\n")
            elif command == "type":
                newPath = checkPath(path, arg)
                if arg in d.keys():
                    print(f"{arg} is a shell {d.get(arg)}")
                elif not newPath == "invalid":
                    print(f"{arg} is {newPath}/{arg}")
                else:
                    print(f"{arg}: not found")


if __name__ == "__main__":
    main()

import sys
d = {
    "exit 0": "valid" 
}

def main():
    exit = False
    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        command = input()
        if command not in d:
            print(f"{command}: command not found")
        if command == "exit 0":
            sys.exit(0)

if __name__ == "__main__":
    main()

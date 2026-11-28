import sys
def pprint(a):
    sys.stdout.write(str(a)+"\n")
stack = []
for i in range(int(sys.stdin.readline().strip())):
    command = sys.stdin.readline().strip()

    if command.startswith("1"):
        stack.append( int(command.split()[1]))
    elif command == "2":
        if len(stack) != 0:
            pprint(stack[-1])
            stack.pop(-1)
        else:
            pprint(-1)
    elif command == "3":
        pprint(len(stack))
    elif command == "4":
        pprint(1 if len(stack) == 0 else 0)
    elif command == "5":
        if len(stack) != 0:
            pprint(stack[-1])
        else:
            pprint(-1)
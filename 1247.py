for _ in range(3):
    result = 0
    for i in range(int(input())):
        result += int(input())
    if result == 0:
        print(0)
    elif result < 0:
        print("-")
    else:
        print("+")
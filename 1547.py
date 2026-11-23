ball = 1

for i in range(int(input())):
    a, b = input().split()
    if int(a) == ball:
        ball = int(b)
    elif int(b) == ball:
        ball = int(a)

print(ball)
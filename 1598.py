a, b = map(int, input().split())

# 표에서 숫자의 위치를 구하기
def get_pos(n):
    x, y = 0, 0
    for i in range(1, 4+1):
        if (n-i)%4 == 0:
            x = (n-i)//4
            y = i
        
    return (x, y)

ap, bp = get_pos(a), get_pos(b)

print(abs(ap[0] - bp[0]) + abs(ap[1] - bp[1]))
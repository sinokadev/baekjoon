# 그 수열의 n번째 숫자가 뭘까
# 1번째 숫자는 1, 2번째 숫자는 2, 3번째 숫자는 2, 4번째 숫자는 3
# n에서 1을 빼고, 2를 빼고, 3을 빼고 .... 
# n = 6
# n -= 1, n = 5
# n -= 2, n = 4
# n -= 3, n = 1
# n -= 4, n이 음수가 됨
# 그러면 6번쨰 숫자는 3이다 라는 가설
# n = 7
# 6, 4, 2, -2
# 7번째 숫자는 3? 4인데
# n = 1
# n -= 1, n = 0
# 0이 됐으니까 1번째 숫자는 1
# n = 2
# n -= 1, n = 1
# n -= 2, n = -1
# 2에서 n이 0 이하가 되었으니 2번째 숫자는 2
# n = 3
# 2, 0, -2
# 3번쨰 숫자도 2
# n = 4
# 3, 1, -3
# 3에서 0이하가 되었으니 3
# 이거 맞는것같은데

def get_num(n):
    copy_n = n+1
    i = 1
    while copy_n > 0:
        copy_n -= i
        i += 1

    return i-1

#for i in range(20):
#    print(get_num(i)) # 와 된다 ㅁㅊ

start, end = input().split()
start, end = int(start), int(end)

su = 0

for i in range(start-1, end):
    su += get_num(i)

print(su)

# AC! 역시 구현은 재밌다
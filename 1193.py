# 1/1 1/2 2/1 3/1 2/2 1/3 1/4 2/3 3/2 2/4 5/1 4/2 3/3 2/4 1/5
# x = 4까지는 미리 적어두는게 낫겠다

# 편의상 이제부터 문제에서 주는 입력 x는 n으로 부르겠음

# 분자/분모
# 좌표 x, y에 있는 분수를 구하는 법을 마련하고
# n으로 x, y를 구하는 방법을 알아내면 될듯

# 근데 그냥 분자 = y, 분모 = x네
# 대각선 올라가는 거랑 대각선 내려가는거랑 꺾이는 부분을 분리해서 계산하면 좋을듯
# n = 4부터 대각선 내려가는거 시작
# 대각선 내려가는건 y-1, x+1 (d라고 부름 down이란 뜻)
# 대각선 올라가는건 y+1, x-1 (u이라 부름 up이란 뜻)
# 내려가기 위해 꺾이는건 y+1 (dc라 부름 down, corner)
# 올라가기 위해 꺾이는건 x+1 (uc라 부름 up, corner)
# n = 4부터 시작하니 d을 할 차례
# d를 2번 하면 uc를 해야함
# uc 하고 u를 3번 해야하고 dc하고 d를 4번
# 규칙은 이건가 d d uc u u u dc d d d d uc u u u u u dc d...
# 그럼 n-3을 일단 하고 1-based로 생각을 하자
# 제한시간이 0.5초니까 한번씩 다 돌려보는건 힘들듯
# 코너링 포함해서 한턴에 3번, 4번, 5번, 6번씩 소요됨
# 근데 한번씩 다 돌려보는게 힘든가?
# 0.5초면 할만할듯 그러면 n-3번 반복하면서 저걸 해보자 한번

n = int(input())

if n == 1: print("1/1");exit()
if n == 2: print("1/2");exit()
if n == 3: print("2/1");exit()
if n == 4: print("3/1");exit()


isdown = True
iscorner = True

x = 2
y = 2

for i in range(n-3):
    if i == 0:
        continue
    if i == 1:
        continue


    if y == 1 and iscorner: # uc
        x+=1
        isdown = False
        iscorner = False
        #print("uc", x, y)
    elif x == 1 and iscorner: # dc
        y += 1
        isdown = True
        iscorner = False
        #print("dc", x, y)
    elif isdown:
        y-=1
        x+=1
        iscorner = True
        #print("d", x, y)
    else:
        y+=1
        x-=1
        iscorner = True
        #print("u", x, y)

print(f"{y}/{x}")
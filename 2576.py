su = 0
lis = []

for i in range(7):
    a = int(input())
    if a%2 != 0: su+=a; lis.append(a)

if su == 0: print(-1)
else: print(f"{su}\n{min(lis)}")
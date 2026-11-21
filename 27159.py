n = int(input())
lis = list(map(int, input().split()))

su = 0
isis = True

for i in range(1, n):
    if abs(lis[i]-lis[i-1]) == 1 and isis:
        su += lis[i]
        isis = False
    else:
        isis = True
        
print(su)
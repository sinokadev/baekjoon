n = int(input())
lis = list(map(int, input().split()))

liss = [[lis[0]]]

ind = 0

for i in range(1, n):
    if abs(lis[i]-lis[i-1]) == 1:
        liss[ind].append(lis[i])
    else:
        liss.append([lis[i]])
        ind += 1
        isis = False

su = 0

for i in liss:
    if i:
        su += i[0]

print(su)
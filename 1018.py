n, m = map(int, input().split())

w, b = 0, 0

white = True

for i in range(n):
    inp = input()
    for j in range(m):
        if i%2 == 0:
            now_w = "W" if j%2 == 0 else "B"
            now_b = "B" if j%2 == 0 else "W"
            #print(i, j, now_w)
            if inp[j] == now_w: w += 1
            elif inp[j] == now_b: b+=1
        else:
            now_b = "W" if j%2 == 0 else "B"
            now_w = "B" if j%2 == 0 else "W"
            #print(i, j, now_w)
            if inp[j] == now_w: w += 1
            elif inp[j] == now_b: b+=1
    
        
print(min(w, b))

###### 8*8 로 자르는거 남음
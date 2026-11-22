#   FF    
#   FF    
# LLDDRRTT
# LLDDRRTT
#   BB    
#   BB    
# 
# 01
# 23

# 0     1     2     3     4     5
# front left  down  right top   back

now = [[],[],[],[],[],[]]
result = [[],[],[],[],[],[]]

for _ in range(2):
    tmp = input().split("|")
    now[0] += tmp[0].strip()[0:2]
    result[0] += tmp[1].strip()[0:2]

for _ in range(2):
    tmp = input().split("|")
    l, r = tmp[0].strip(), tmp[1].strip()
    now[1] += l[0:2]; now[2] += l[2:4]; now[3] += l[4:6]; now[4] += l[6:8]
    result[1] += r[0:2]; result[2] += r[2:4]; result[3] += r[4:6]; result[4] += r[6:8]

for _ in range(2):
    tmp = input().split("|")
    now[5] += tmp[0].strip()[0:2]
    result[5] += tmp[1].strip()[0:2]

print(now, result)

###### 푸는중
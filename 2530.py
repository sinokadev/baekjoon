a,b,c = map(int,input().split())
d = int(input())

cho = a*(60*60) + b*60 + c + d

si = cho//(60*60)
bun = (cho%(60*60))//60
ccho = (cho%(60*60))%60

while si >= 24:
    si -= 24
    
print(si, bun, ccho)
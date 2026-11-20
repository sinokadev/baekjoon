n = int(input())

inp = list(map(int,input().split()))

dp = [inp[0]]

for i in range(1, n):
    if dp[i-1] < 0:
        dp.append(inp[i])
    else:
        dp.append(dp[i-1] + inp[i])

print(max(dp))
n = int(input())
strs = [input()]
result = list(strs[0])

for i in range(n-1):
    strs.append(input())
    now = strs[-1]

    for ind in range(len(now)):
        if result[ind] != now[ind]:
            result[ind] = "?"
        elif result[ind] == "?": pass


print("".join(result))
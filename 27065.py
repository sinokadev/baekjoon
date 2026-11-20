def yaksu(n):
    yaksus = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            yaksus.append(i)
            yaksus.append(n//i)

    return sorted(list(set(yaksus)))

for i in range(int(input())):
    n = int(input())
    yaksus = yaksu(n)[:-1]
    sumyak = sum(yaksus)

    if not n < sumyak:
        print("BOJ 2022")
    else:
        result = "Good Bye"
        for j in yaksus:
            if j < sum(yaksu(j)[:-1]):
                result = "BOJ 2022"
                break
        print(result)
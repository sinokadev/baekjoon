while (inp := input()) != "# 0 0":
    a,b,c = inp.split()
    if int(b) > 17: print(a, "Senior")
    elif int(c) >= 80: print(a, "Senior")
    else: print(a, "Junior")
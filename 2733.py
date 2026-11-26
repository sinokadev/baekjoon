def run(code: str):
    array = bytearray(32768)
    pointer = 0
    pc = 0
    result = ""

    loopmap = {}

    depth = []

    # 전처리 (괄호 짝 찾고, 짝 안맞으면 컴파일에러 띄우고, 어디에 있는 "["를 만났을때 pc를 뭐로 설정해야하는지 등 미리 정해놓는)
    for i, char in enumerate(code):
        if char == "[":
            depth.append(i)
        elif char == "]":
            if len(depth) <= 0:
                return "COMPILE ERROR"
            loopmap[depth[-1]] = i
            del depth[-1]

    if len(depth) > 0:
        return "COMPILE ERROR"

    # 뒤집힌 loopmap 생성
    reverse_loopmap = {v: k for k, v in loopmap.items()}

    # 실행
    while pc < len(code):
        match code[pc]:
            case ">":
                if pointer == 32767:
                    pointer = 0
                else:
                    pointer += 1
            case "<":
                if pointer == 0:
                    pointer = 32767
                else:
                    pointer -= 1
            case "+":
                if array[pointer] == 255:
                    array[pointer] = 0
                else:
                    array[pointer] += 1
            case "-":
                if array[pointer] == 0:
                    array[pointer] = 255
                else:
                    array[pointer] -= 1
            case ".":
                result += chr(array[pointer])
            case "[":
                if array[pointer] == 0:
                #    ind = code[pc:-1].find("]")
                #    if ind != -1:
                #        pc = ind
                    pc = loopmap[pc]
            case "]":
                if array[pointer] != 0:
                #    ind = code[0:pc].rfind("[")
                #    if ind != -1:
                #        pc = ind
                    pc = reverse_loopmap[pc]
        pc+=1
    return result

for i in range(int(input())):
    code = ""
    while (inp := input()) != "end":
        ind = inp.find("%")
        if ind != -1:
            code += inp[0:ind]
        else:
            code += inp
    code.replace("\n", "")
    print(f"PROGRAM #{i+1}:\n{run(code)}")
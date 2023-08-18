T = 10
for tc in range(1, 11):
    N = int(input())
    code = list(map(int, input().split()))

    # for i in range(max(code)*10000):         # 1, 2, 3, 4, 5
    i = 0
    while True:
        j = i % 5 + 1
        new_num = code.pop(0) - j
        code.append(new_num)
        i += 1
        if code[-1] < 0:
            code[-1] = 0
            break
        elif code[-1] == 0:
            break

    code = map(str, code)
    result = " ".join(code)
    print(f'#{tc} {result}')
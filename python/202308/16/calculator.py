# 계산기1
# SWEA 난이도 D4

t = 10
for tc in range(1, t+1):
    n = int(input())
    arr = list(input())

    arr[0], arr[1] = arr[1], arr[0]
    arr.pop(0)
    arr.append('+')
    stack = []
    for x in arr:
        if '0'<=x<='9':
            stack.append(int(x))
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b)
    print(f'#{tc} {stack.pop()}')
    
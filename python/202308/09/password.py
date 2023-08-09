# 비밀번호
# SWEA 난이도 : D3

t = 10
for tc in range(1, t+1):
    leng, string = input().split()
    leng = int(leng)
    stack = []

    for i in range(leng):
        if not stack or stack[-1] != string[i]:
            stack.append(string[i])
            continue
        stack.pop()

    print(f'#{tc} {"".join(stack)}')
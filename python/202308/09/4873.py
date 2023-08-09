# 반복문자 지우기
# SWEA 난이도 : D2

# 문자열 s에서 연결된 문자 지우기
# 지운 후 남은 문자열의 길이 출력

t = int(input())
for tc in range(1, t+1):
    string = input()
    stack = []

    for i in range(1, len(string)):
        if not stack or (stack and stack[-1] != string[i]) :
            stack.append(string[i])
            continue
        elif stack[-1] == string[i]:
            stack.pop()
            

    print(f'#{tc} {len(stack)}')



# 괄호 검사
# SWEA 난이도 D2

# {}, () 짝 이뤘는지 검사하는 프로그램

t = int(input())
for tc in range(1, t+1):
    line = input()
    stack = []
    answer = 1
    for x in line:
        if x == '(' or x == '{':
            stack.append(x)
        elif x == ')':
            if not stack or stack.pop() != '(':
                answer = 0
                break
        elif x == '}':
            if not stack or stack.pop() != '{':
                answer = 0
                break
    if stack:
        answer = 0

    print(f'#{tc} {answer}')

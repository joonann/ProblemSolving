# forth 
# SWEA 난이도 D1

t = int(input())
for tc in range(1, t+1):
    answer = 0
    s = list(input().split())

    stack = []
    for i in range(len(s) - 1):
        if s[i] not in '+-*/':
            stack.append(int(s[i]))
        else:
            if len(stack) < 2 :
                answer = 'error'
                break
            b = int(stack.pop())
            a = int(stack.pop())
            if s[i] == '+':
                stack.append(str(a+b))
            elif s[i] == '-':
                stack.append(str(a-b))
            elif s[i] == '/':
                stack.append(str(a//b))
            elif s[i] == '*':
                stack.append(str(a*b))

    if answer != 'error' and len(stack) == 1:
        answer = stack.pop()
    else:
        answer = 'error'
    print(f'#{tc} {answer}')
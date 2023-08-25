'''
단순2진암호코드
암호코드 8개 숫자
(홀수 자리의 합x3) + (짝수 자리의 합)이 10의 배수가 되어야함

'''

code = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

def pw_sum(password): # password에 int 리스트 넣어야됨
    odd_flag = True
    password_sum = 0
    print_sum = 0
    for i in range(len(password)):
        if odd_flag:
            password_sum += password[i] * 3
            print_sum += password[i]
        else:
            password_sum += password[i]
            print_sum += password[i]
        odd_flag = not odd_flag
    if password_sum % 10 == 0:
        return print_sum
    return 0

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        s = list(map(int,input()))
        if len(a) == 0:
            for i in range(m-1, -1, -1):
                if s[i] == 1:
                    start, end = i-55, i+1
                    a = s[i-55:i+1]
                    break

    answer = []
    for i in range(8):
        t = ''.join(map(str, list(a[i*7:i*7+7])))
        answer.append(code.index(t))
    print(f'#{tc} {pw_sum(answer)}')
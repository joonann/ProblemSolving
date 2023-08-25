'''
이진수 SWEA D2
십진수 N을 2진수로 바꾸기
'''

t = int(input())
for tc in range(1, t+1):
    n = float(input())
    a = 0.5
    answer = ''
    
    for _ in range(12):
        if n <= 0:
            break
        if n >= a:
            answer += '1'
            n -= a
        else:
            answer += '0'
        a /= 2
    if n > 0:
        answer = 'overflow'
    print(f'#{tc} {answer}')
'''
이진수 SWEA D2

16진수 > 2진수로 표시
'''

hex = '0123456789ABCDEF'

t = int(input())
for tc in range(1, t+1):
    _, x = input().split()
    print(f'#{tc}', end=' ')
    for a in x:
        i = hex.index(a)
        j = 8
        for _ in range(4):
            print(i//j, end='')
            i%=j
            j//=2
    print()

'''
컨테이너 운반
SWEA 5201 D2
'''

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    w = sorted(list(map(int, input().split())), reverse=True)
    t = sorted(list(map(int, input().split())), reverse=True)
    ans = 0
    i = 0
    for x in w:
        if i < m and x <= t[i]:
            ans += x
            i += 1
    print(f'#{tc} {ans}')
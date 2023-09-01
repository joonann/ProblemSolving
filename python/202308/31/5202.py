'''
화물 도크
SWEA 5202 D2
'''

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda x: (x[1], x[0]))
    ans = 0
    end = 0
    for x in arr:
        if x[0] < end:
            continue
        ans += 1
        end = x[1]

    print(f'#{tc} {ans}')
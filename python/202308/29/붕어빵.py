t = int(input())
for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    ti = list(map(int, input().split()))
    ti.sort()

    result = 'Possible'
    for i in range(n):
        b = ti[i]//m*k
        if b < i+1:
            result = 'Impossible'
            break

    print(f'#{tc} {result}')
        
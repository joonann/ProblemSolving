# 종이 붙이기
# SWEA 4869
# 난이도 : D2

t = int(input())
for tc in range(1, t+1):
    n = int(input()) // 10
    fb = [0] * (n+1)
    fb[0] = 0
    fb[1] = 1
    fb[2] = 3
    for i in range(3, n+1):
        fb[i] = fb[i-1] + fb[i-2] * 2

    print(f'#{tc} {fb[n]}')
# 회문1
# SWEA
# 난이도 : D3

t = 10
for tc in range(1, t+1):
    m = int(input())
    n = 8
    graph = [list(input()) for _ in range(n)]

    count = 0

    for i in range(n):
        for j in range(n - m + 1):
            for k in range(m // 2 + 1):
                if graph[i][j+k] != graph[i][j+m-1-k]:
                    break
                if k == m // 2:
                    count += 1

    for i in range(n-m+1):
        for j in range(n):
            for k in range(m // 2 + 1):
                if graph[i+k][j] != graph[i+m-1-k][j]:
                    break
                if k == m // 2:
                    count += 1
    print(f'#{tc}', count)
# 파스칼의 삼각형

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    graph = [[0] * (i+1) for i in range(n)]
    for i in range(0, n):
        graph[i][0] = graph[i][-1] = 1
        for j in range(1, i):
            graph[i][j] = graph[i-1][j] + graph[i-1][j-1]

    print(f'#{tc}')
    for i in range(n):
        print(*(graph[i]))

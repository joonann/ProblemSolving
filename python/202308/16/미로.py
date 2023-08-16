# 미로 
# SWEA 난이도 D3

# N x N 크기 미로
# 출발지에서 도착지 경로 존재 >> 1
# 존재 안하면 0

# 0 통로 1 벽 2 출발 3 도착

d = ((0, 1), (1, 0), (0, -1), (-1, 0))

def dfs(now, visited, is_found):
    global answer
    i, j = now
    if is_found:
        return
    if graph[i][j] == 3:
        answer = 1
        is_found = True
        return
    for a, b in d:
        ni, nj = i+a, j+b
        if 0<=ni<n and 0<=nj<n and visited[ni][nj] == False \
            and graph[ni][nj] != 1:
            visited[ni][nj] = True
            dfs((ni, nj), visited, is_found)
            visited[ni][nj] = False


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    graph = [list(map(int, input())) for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]

    start = 0

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 2:
                start = (i, j)
                visited[i][j] = True
                break
        if start:
            break

    answer = 0
    is_found = False
    dfs(start, visited, is_found)
    
    print(f'#{tc} {answer}')
# 미로 
# SWEA 난이도 D3

# N x N 크기 미로
# 출발지에서 도착지 경로 존재 >> 1
# 존재 안하면 0

# 0 통로 1 벽 2 출발 3 도착

d = ((0, 1), (1, 0), (0, -1), (-1, 0))

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    graph = [list(map(int, input())) for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]

    q = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 2:
                graph[i][j] = 0
                q = [(i, j)]
                visited[i][j] = True
                break
        if q:
            break

    answer = 0
    is_found = False
    while q:
        if is_found:
            break
        x, y = q.pop(0)
        for i, j in d:
            nx, ny = x + i, y + j
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    visited[nx][ny] = True
                    q.append((nx, ny))
                elif graph[nx][ny] == 3:
                    answer = graph[x][y]
                    is_found = True
                    break

    print(f'#{tc} {answer}')
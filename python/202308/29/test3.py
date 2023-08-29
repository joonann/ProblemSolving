
# 아래 오른쪽 위 왼쪽
# bfs의 경우 앞에서 pop하기 때문에 왼쪽 오른쪽 위 아래 순서로 탐색
# d = ((1, 0), (0, 1), (-1, 0), (0, -1))
# dfs의 경우 뒤에서 pop하기 때문에 아래 델타 사용
d = ((0, -1), (-1, 0), (0, 1), (1, 0))


n, m = map(int, input().split())
graph = [[0]*(m+1)]
for _ in range(n):
    graph.append([0]+list(map(int, input())))
visited = [[False]*(m+1) for _ in range(n+1)]

q = [(1, 1)]

while q:
    x, y = q.pop()
    if not visited[x][y]:
        visited[x][y] = True
        
        for a, b in d:
            nx, ny = x + a, y + b
            if 1<=nx<=n and 1<=ny<=m and not visited[nx][ny]\
                and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1


for i in graph:
    print(i)
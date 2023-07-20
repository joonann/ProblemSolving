# 적록색약
# 백준 10026
# 난이도 : 골드5

# N x N 그리드에 R, G, B
# 적록색약이 아닌 사람이 본 구역 개수, 적록색약인 사람이 본 구역 개수 출력

from collections import deque
import sys

input = sys.stdin.readline

# 동서남북
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

N = int(input())

# 일반 그리드 테이블 입력
grid = [list(input()) for _ in range(N)]

queue = deque() # 얘를 밖으로 빼니까 메모리초과는 안 나네?
# B_count = 0
# RG_count = 0
# R_count = 0
# G_count = 0
res1 = res2 = 0

def bfs(this_grid, a, b):
    queue.append((a, b))
    color = this_grid[a][b]
    RG_mixed = False
    while queue:
        x, y = queue.popleft()
        if this_grid[x][y] in 'RG':
            this_grid[x][y] = 'C'
        elif this_grid[x][y] == 'B':
            this_grid[x][y] = 'D'
        else:
            this_grid[x][y] = '0'
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and this_grid[nx][ny] == color:
                queue.append((nx, ny))

for i in range(N):
    for j in range(N):
        if grid[i][j] in 'RGB':
            bfs(grid, i, j)
            res1 += 1

print(grid)

for i in range(N):
    for j in range(N):
        if grid[i][j] == 'CD':
            bfs(grid, i, j)
            res2 += 1

print(res1, res2)
# 1트 
# 시간초과가 난다.
# 일반과 적록색약 테이블 따로 bfs하지 않고 한번에 하는 방법을 찾아보자

# B일 때 먼저 bfs 수행하고
# R, G 일 때 bfs 수행하면서 두 색깔을 한 문자'C'로 바꿔준다.
# C일 때 bfs를 마지막으로 수행하면 중복이 줄지 않을까

# 2트 
# 시간초과는 해결했는데 메모리초과가 발생한다.


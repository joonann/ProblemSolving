# 미로 탐색
# 백준 2178
# 난이도 : 실버1

# N x M 크기의 미로
# 1 > 이동 가능
# 0 > 이동 불가능
# (1, 1)에서 (N, M)으로 가는 최소 이동 경로

import sys
from collections import deque

input = sys.stdin.readline

# 동서남북
dy = (0, 0, 1, -1)
dx = (1, -1, 0, 0)

N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, input().rstrip()))) 
# readline의 경우 맨 뒤에 '\n'까지 입력받으므로 제거해줘야 함
# strip 메서드 사용

visited = [[False for _ in range(M)] for _ in range(N)]

queue = deque()
queue.append((0, 0))
visited[0][0] = True
while queue:
    a, b = queue.popleft()
    for i in range(4):
        y = a + dy[i]
        x = b + dx[i]
        if y < 0 or y >= N or x < 0 or x >= M:
            continue
        if maze[y][x] == 1:
            if visited[y][x]:
               continue
            visited[y][x] = True
            maze[y][x] = maze[a][b] + 1
            queue.append((y, x))

print(maze[N-1][M-1])

# deque를 사용해 BFS 알고리즘 구현
# queue라는 list에서 pop을 하면 맨 뒤 요소를 가져오기 때문에
# deque를 사용했음.
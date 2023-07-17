# 미로 탐색
# 난이도 : 실버1

# N x M 크기의 미로
# 1 > 이동 가능
# 0 > 이동 불가능
# (1, 1)에서 (N, M)으로 가는 최소 이동 경로

import sys

input = sys.stdin.readline

# 동서남북
dy = (0, 0, 1, -1)
dx = (1, -1, 0, 0)

N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
visitied = [[False for _ in range(N)] for _ in range(M)]


queue = []
queue.push((0, 0))
def bfs(position):
    a, b = queue.pop()
    if visited[a][b]:
        return
    visited[a][b] = True
    

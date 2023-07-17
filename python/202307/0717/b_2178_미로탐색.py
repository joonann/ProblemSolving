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
visited = [[False for _ in range(N)] for _ in range(M)]

queue = []
distance = 0

queue.append((0, 0))
while queue:
	a, b = queue.pop()
	if a == N-1 and b == M-1:
		break
	if visited[a][b] != True:
		visited[a][b] = True
		distance += 1
		for i in range(4):
			y, x = a + dy[i], b + dx[i]
			if (y < 0 or y >= N or x < 0 or x >= M):
				continue
			queue.append((y, x))

print(distance)

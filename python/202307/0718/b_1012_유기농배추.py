# 유기농배추
# 백준 1012
# 난이도 : 실버2

# 인접해있는 1 묶음의 개수 구하기

from collections import deque

# 동서남북
dy = (0, 0, 1, -1)
dx = (1, -1, 0, 0)

# bfs 코드
def bfs(X, Y):
    queue = deque([])
    queue.append((X, Y))
    field[X][Y] = 0
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if field[nx][ny] == 1:
                field[nx][ny] = 0
                queue.append((nx, ny))

# 테스트 케이스 개수
T = int(input())

for _ in range(T):
    # 가로 N, 세로 M, 배추(1)의 개수 K
    N, M, K = map(int, input().split())

    # 밭 테이블
    field = [[0 for _ in range(N)] for _ in range(M)]

    # 배추의 위치
    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1

    worm = 0

    for a in range(M):
        for b in range(N):
            if field[a][b] == 1:
                bfs(a, b)
                worm += 1

    print(worm)
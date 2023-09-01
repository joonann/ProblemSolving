'''
물놀이를 가자
n x m 크기 격자
물 W 땅 L
땅으로 표현된 모든 칸에 대해서 어떤 물인 칸으로 이동하기 이동횟수의 합 출력

'''
from collections import deque

d = ((0, -1), (0, 1), (1, 0), (-1, 0))

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    graph = [input() for _ in range(n)] # 리스트 함수 때문에 시간초과 난다.
    visited = [[-1]*m for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'W':
                q.append((i, j))
                visited[i][j] = 0

    while q:
        i, j = q.popleft()
        for a, b in d:
            ni, nj = i+a, j+b
            if 0<=ni<n and 0<=nj<m and visited[ni][nj] == -1 and graph[ni][nj] == 'L':
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1

    ans = 0
    for i in range(n):
        for j in range(m):
            ans += visited[i][j]

    print(f'#{tc} {ans}')
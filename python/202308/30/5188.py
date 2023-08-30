'''
최소합
SWEA D3 
완전탐색 숫자들 최소합
'''
from collections import deque

d = ((0, 1), (1, 0))

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    min_sum = [[0]*n for _ in range(n)]
    
    q = deque([(0, 0)])
    min_sum[0][0] = graph[0][0]
    while q:
        x, y = q.popleft()
        if x == n-1 and y == n-1:
            break
        for a, b in d:
            nx, ny = x+a, y+b
            if 0<=nx<n and 0<=ny<n:
                
                if min_sum[nx][ny]:
                    min_sum[nx][ny] = min(min_sum[nx][ny], min_sum[x][y] + graph[nx][ny])
                else:
                    min_sum[nx][ny] = min_sum[x][y] + graph[nx][ny]
                    q.append((nx, ny))

    print(f'#{tc} {min_sum[n-1][n-1]}')        





    
    
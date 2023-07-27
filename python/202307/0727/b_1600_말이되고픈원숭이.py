# 말이 되고픈 원숭이
# 백준 1600
# 난이도 : 골드 3

from collections import deque
import sys
input = sys.stdin.readline

# (네 방향만) 
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0) 

# (여덟 방향 나이트 이동)
knightx = (-2, -1, 1, 2, 2, 1, -1, -2)
knighty = (1, 2, 2, 1, -1, -2, -2, -1)

# 나이트처럼 이동할 수 있는 수
k = int(input())
w, h = map(int, input().split())

# 격자판 입력
map1 = [list(map(int, input().split())) for _ in range(h)]
visited = [[False for _ in range(w)] for _ in range(h)]

min1 = [[0 for _ in range(w)] for _ in range(h)] ######

# 맵 안에 있어야 되고
# 장애물 1이면 안 되고
# visited가 False여야 됨
def ispossible(a, b):
    if 0 <= a < h and 0 <= b < w:
        if map1[a][b] == 0:
            if visited[a][b] == False:
                return True
    return False

result = 0

q = deque()
# a, b 좌표, 나이트 움직임 횟수, 총 움직임 횟수
q.append((0, 0, 0, 0))
visited[0][0] = True

result = -1

if map1[0][0] == 0:
    # bfs
    while q:
        # 현재 위치
        a, b, knight_move_now, move_now = q.popleft()
        if a == h - 1 and b == w - 1:
            result = move_now
            break
        
        # 현재 나이트 이동 횟수가 남아있는 경우,
        if knight_move_now < k:
            for i in range(8):
                na, nb = a + knightx[i], b + knighty[i]
                # 갈 수 있으면 q에 append
                if ispossible(na, nb):
                    visited[na][nb] = True
                    q.append((na, nb, knight_move_now + 1, move_now + 1))
                    min1[na][nb] = move_now + 1 ####

        # 동서남북도 마찬가지 조건을 확인해서 q에 append
        for i in range(4):
            na, nb = a + dx[i], b + dy[i]

            if ispossible(na, nb):
                visited[na][nb] = True
                q.append((na, nb, knight_move_now, move_now + 1))
                min1[na][nb] = move_now + 1 ####

print(result)
for i in range(h):
    print(min1[i])

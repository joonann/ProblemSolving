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
visited = [[[0] * (k + 1) for _ in range(w)] for _ in range(h)]

# 맵 안에 있어야 되고
# 장애물 1이면 안 되고
# visited가 False여야 됨
def ispossible(a, b):
    if 0 <= a < h and 0 <= b < w:
        if map1[a][b] == 0:
            return True
    return False

result = 0

q = deque()
# a, b 좌표, 나이트 움직임 횟수, 총 움직임 횟수
q.append((0, 0, 0))
# if visited 여부로 판단할 것이기 때문에 처음 이동횟수 1로, 나중에 1 빼줘야 된다.
visited[0][0][0] = 1

result = -1

if map1[0][0] == 0:
    # bfs
    while q:
        # 현재 위치
        a, b, knight_move_now = q.popleft()
        if a == h - 1 and b == w - 1:
            result = visited[a][b][knight_move_now] - 1
            break

        # 동서남북 먼저 조건을 확인해서 q에 append
        for i in range(4):
            na, nb = a + dx[i], b + dy[i]

            if ispossible(na, nb):
                if not visited[na][nb][knight_move_now]:
                    visited[na][nb][knight_move_now]
                q.append((na, nb, knight_move_now))
        
        # 현재 나이트 이동 횟수가 남아있는 경우,
        if knight_move_now < k:
            for i in range(8):
                na, nb = a + knightx[i], b + knighty[i]
                # 갈 수 있으면 q에 append
                if ispossible(na, nb):
                    if not visited[na][nb][knight_move_now + 1]:
                        visited[na][nb][knight_move_now + 1] \
                            = visited[a][b][knight_move_now] + 1
                    q.append((na, nb, knight_move_now + 1))


print(result)


# visited를 3차원 배열로 만들어서 knight 이동의 횟수도 점점 늘려가주는 방법을 사용해야 한다.
# 그렇지 않으면 최소 이동 횟수만 생각하기 때문에 knight이동으로 먼저간 곳은 동서남북 이동으로 방문하지
# 않는다. 

# 집가서 디버깅하자
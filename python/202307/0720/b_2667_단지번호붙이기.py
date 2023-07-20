# 단지번호붙이기
# 백준 2667
# 난이도 : 실버1

# N x N 크기의 지도
# 1 = 집
# 0 = 집이 없는 곳
# 상하좌우로 이어져있는 단지수 출력, 단지별 집의 수를 오름차순 정렬 출력

from collections import deque

# 동서남북
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

N = int(input())
# 단지 지도 입력
apart_map = [list(map(int, input())) for _ in range(N)]
# 단지 개수
apart_count = 0
# 단지별 집 개수 리스트
apart_house_counts = []

#BFS 코드
def bfs(x, y):
    house_count = 0
    queue = deque([(x, y)]) # 매개변수 iterable을 deque 객체로 변환
    apart_map[x][y] = 0
    while queue:
        a, b = queue.popleft()
        house_count += 1
        
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                if apart_map[nx][ny] == 1:
                    queue.append((nx, ny))
                    apart_map[nx][ny] = 0
    return house_count                    

for i in range(N):
    for j in range(N):
        if apart_map[i][j] == 1:
            apart_house_counts.append(bfs(i, j))
            apart_count += 1

apart_house_counts.sort()
print(apart_count)
for a in apart_house_counts:
    print(a)

'''
마법사 상어와 비바라기
백준 21610
난이도 골드 5


'''
import sys
input = sys.stdin.readline

# 8개의 방향(9시방향에서 시작) (나머지연산 사용할 것)
cloud_move = ((), (0, -1), (-1, -1), (-1, 0), (-1, 1),\
               (0, 1), (1, 1), (1, 0), (1, -1))
# 대각선 인접 좌표
x_d = ((-1, -1), (-1, 1), (1, -1), (1, 1))

# nxn 만큼의 바구니, m만큼 이동
n, m = map(int, input().split())
baskets = [list(map(int, input().split())) for _ in range(n)]
moves = [tuple(map(int, input().split())) for _ in range(m)]


# 초기 구름의 좌표들
cloud = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]

# m번 이동하면서
for dir, dist in moves:

    visited = [[False] * n for _ in range(n)]
    # 구름 이동
    # for j in range(len(cloud)):
    #     cloud[j][0] = (cloud[j][0] + dist * cloud_move[dir][0]) % n
    #     cloud[j][1] = (cloud[j][1] + dist * cloud_move[dir][1]) % n
    #     # 비가 내린다
    #     baskets[cloud[j][0]][cloud[j][1]] +=1
    # 여러번 참조해서 더 시간이 오래걸린다.
    # 궁극적으로는 얘보다 visited로 멤버쉽 연산자 대체하는 게 더 최적화에 유리할지도 

    moved_cloud = []
    for a, b in cloud:
        na = (a + cloud_move[dir][0] * dist) % n
        nb = (b + cloud_move[dir][1] * dist) % n
        baskets[na][nb] += 1
        moved_cloud.append((na, nb))
        visited[na][nb] = True

    # 물복사버그 마법 시전(대각선 방향 확인한다.)
    for a, b in moved_cloud:
        for da, db in x_d:
            na, nb = a + da, b + db
            if 0<=na<=n-1 and 0<=nb<=n-1 and baskets[na][nb]:
                baskets[a][b] += 1 
    
    new_cloud = []
    # 다음 구름을 지정해준다.
    for a in range(n):
        for b in range(n):
            # is_not_visited = True
            # for x, y in moved_cloud:
            #     if a == x and b == y:
            #         is_not_visited = False
            #         break

            if not visited[a][b] and baskets[a][b] >= 2:
                new_cloud.append((a, b))
                baskets[a][b] -= 2
    cloud = new_cloud

# 답안 출력
ans = 0
for a in range(n):
    for b in range(n):
        ans += baskets[a][b]
print(ans)
# print(sum(map(sum, baskets)))
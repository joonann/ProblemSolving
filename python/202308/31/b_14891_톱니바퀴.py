'''
톱니바퀴
백준 14891
난이도 골드5

4개(1, 2, 3, 4번)의 톱니바퀴(8개 톱니)
N극/S극
톱니바퀴를 K번 회전(시계/반시계)
인접한 톱니바퀴와 만나는 톱니가 
1. 같은 극이면 회전하지 않는다.
2. 다른 극이면 반대방향으로 회전한다.

'''
s = [[], [7, 0, -1], [0, 7, 1]]

def rotate(gear1, s_d):
    start, end, step = s_d
    tmp = gear1[start]
    for i in range(start, end, step):
        gear1[i] = gear1[i + step]
    gear1[end] = tmp

gear = [[]]+[list(map(int, input())) for _ in range(4)]
k = int(input())

for _ in range(k):
    gear_num, d = map(int, input().split())
    q = [(gear_num, d)]
    r = []
    visited = [1, 0, 0, 0, 0, 1]
    # bfs 
    while q:
        gn, d = q.pop(0)
        if not visited[gn]:
            r.append((gn, d))
            visited[gn] = 1
            for a in [-1, 1]:
                ngn = gn + a
                if not visited[ngn] and\
                    gear[gn][0+2*a] != gear[ngn][0-2*a]:
                    q.append((ngn, -d))
                    
    for gn1, d1 in r:
        rotate(gear[gn1], s[d1])

answer = 0
for i in range(1, 5):
    if gear[i][0] == 1:
        answer += 1<<(i-1)
print(answer)

# rotate(gear[1], s[1]) 이런 식으로 시계방향 회전
# rotate(gear[1], s[-1]) 이런 식으로 시계반대방향 회전




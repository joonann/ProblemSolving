'''
로봇 청소기
백준 14503
골드 5

n x m 크기의 직사각형 방 (0,0) ~ (n-1,m-1)
벽 또는 빈칸
청소기 바라보는 방향 동서남북
빈칸을 청소해야됨

1. 현재 칸 빈칸이면 청소(2로 바꿈)
    주변 4칸 빈칸 체크
    2-1. 주변 4칸 중 빈칸이 없으면 후진하고 1번으로
        후진 불가능하면 작동 멈춤
    2-2. 주변 4칸 중 빈칸이 있으면 반시계방향으로 90도 회전 
        앞칸이 빈칸이면 전진하고 1번으로

n, m 방의 크기
r, c, d 로봇청소기의 위치(항상 빈칸)와 방향 주어짐
n개 줄에 방의 위치
'''

# 북 동 남 서 (반시계방향의 경우 +3 >> % 4)
delta = [0, 1, 2, 3]
four = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def clean(graph, now, d, n):
    answer = 0
    r, c = now
    while True:
        is_four_cleaned = True
        if graph[r][c] == 0:
            graph[r][c] = 2
            answer += 1
        for a, b in four:
            nr, nc = r+a, c+b
            if graph[nr][nc] == 0:
                is_four_cleaned = False
                break
        if is_four_cleaned:
            a, b = four[(d+2)%4]
            r, c = r+a, c+b
            if graph[r][c] == 1:
                break
        else:
            d = (d + 3) % 4
            a, b = four[d]
            nr, nc = r + a, c + b
            if graph[nr][nc] == 0:
                r, c = nr, nc
    return answer

n, m = map(int,input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

print(clean(graph, (r, c), d, n))
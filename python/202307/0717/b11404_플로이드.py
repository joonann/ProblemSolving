# 백준 11404
# 문제명 : 플로이드
# 난이도 : 골드4
import sys

input = sys.stdin.readline
INF = int(1e9)

# n 개의 도시
n = int(input())
# m 개의 버스
m = int(input())

# 정답으로 출력할 2차원 배열, 거리는 전부 INF로 초기화
bus = [[INF for _ in range(n+1)] for _ in range(n+1)]

# i도시에서 i도시로 가는 시간 0
for i in range(n+1):
    bus[i][i] = 0 

# i 도시에서 출발하는 버스 (j 노선, a 소요시간) 입력
for _ in range(m):
    i, j, a = map(int, input().split())
    # 노선이 여러 개일 수도 있기 때문에 더 적게 걸리는 소요시간으로 입력
    bus[i][j] = min(bus[i][j], a)

# 플로이드 워셜 알고리즘 이용해서 최단 소요시간 입력
for a in range(1, n+1):
    for x in range(n+1):
        for y in range(n+1):
            bus[x][y] = min(bus[x][y], bus[x][a]+bus[a][y])

for i in range(1, n+1):
    for j in range(1, n+1):
        if bus[i][j] == INF:
            bus[i][j] = 0
        print(bus[i][j], end=' ')
    print()
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

graph = [[] for _ in range(n+1)]
for _ in range(m):
    i, j, a = map(int, input().split())
    graph[i].append((j, a))
    # i 도시에서 출발하는 버스 (j 노선, a 소요시간) 추가

# 정답으로 출력할 2차원 배열, 거리는 전부 INF로 초기화
bus_course = [[INF] * (n+1) for i in range(n+1)]

for i in range(1, n+1):
    bus_course[i][i] = 0

print(bus_course)

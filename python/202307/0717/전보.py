import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
# 노드의 개수, 간선의 개수, 시작 노드

graph = [[] for i in range(n+1)]
# 노드 연결 정보 리스트 생성

distance = [INF] * (n+1)
# 최단거리 테이블 초기화

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))
    # x에서 y로 가는 소요시간 z 

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 현재 노드(now)가 처리됐고 
                    # 현재 노드(now)까지 오는 소요시간보다 더 짧은 길이의 경로가 저장돼있다면 넘어가기
            continue
        for i in graph[now]: # 현재 노드(now)가 연결되어 있는 i : (y,z) - y까지 z소요
            cost = dist + i[1]
            if cost < distance[i[0]]: # 현재 노드(now)를 거쳐 i[0] 노드로 이동하는 거리가 더 짧을 경우
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 우선순위큐(heapq)를 이용한 다익스트라 알고리즘
# 쉽게 말해 노드까지 가는 거리(소요시간) 을 최소 heap에 쌓아서
# 그 중에서 가장 짧은 경로만 얻어가는 방법
# heapq 뒤쪽에 쌓인, 최단시간이 아닌 경로들은 continue로 무시된다.

dijkstra(start)

print(distance)
count = 0
max_distance = 0

for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance)
# 도달할 수 있는 노드의 개수, 가장 멀리 있는 노드와의 최단거리
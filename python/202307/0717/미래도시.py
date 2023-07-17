'''
1~N번 회사 간 양방향 도로 연결
연결된 도로 소요시간은 1시간
A가 1번에서 K번 회사 들러서 x번 회사 방문

플로이드 워셜 알고리즘으로 모든 지점에서 다른 모든 지점까지의 최단경로를 구하고
K번 회사 가는 시간 + x번 회사 가는 시간 

'''

INF = int(1e9) # 1e9 쓰는 이유는 2e9 쓰면 두 수를 더했을 때 오버플로우 날 수 있어서

n, m = map(int, input().split())
# 노드 개수, 간선 개수

graph = [[INF] * (n+1) for _ in range(n+1)]
# 2차원 리스트 무한 값으로 생성

# n회사에서 n회사로 가는 비용 : 0
for a in range(1, n+1):
    graph[a][a] = 0

# 각 간선에 대한 정보 입력 
for _ in range(m):
    a, b = map(int, input().split())
    # 가는 소요시간 1시간으로 2차원 리스트에 저장
    graph[a][b] = 1 
    graph[b][a] = 1

# 최종 목적지 x 와 경유지 k 입력
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘 수행
for i in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

distance = graph[1][k] + graph[k][x]           

# 갈 수 없으면 -1, 갈 수 있으면 
if distance == INF:
    print("-1")
else:
    print(distance)
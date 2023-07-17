INF = int(1e9) 

# 헛간 개수, 통로 개수
n, m = map(int, input().split())  

graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

for a in range(1, n + 1):
    graph[a][a] = 0 

for _ in range(m):
    a, b = map(int, input().split())  
    graph[a][b] = 1  
    graph[b][a] = 1 

#플로이드 워셜 알고리즘 수행
for i in range(1, n + 1):  
    for a in range(1, n + 1):  
        for b in range(1, n + 1):  
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

# 헛간까지의 거리
distance = max(graph[1][1:])
# 숨을 헛간 번호
barnNumber = graph[1].index(distance)
# 같은 거리에 있는 헛간 개수
cnt = 0
for i in range(1, n+1):
    if graph[1][i] == distance:
        cnt += 1

print(barnNumber, distance, cnt)
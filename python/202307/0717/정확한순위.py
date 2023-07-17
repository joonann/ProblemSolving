# n명의 성적, 성적 비교 결과 주어짐
# 정확한 성적 순위를 알 수 있는 학생 수 출력

INF = int(1e9)
n, m = map(int, input().split())
answer = 0

# n개의 노드에서 n개의 노드로 이어지는 간선이 있는지 2차원 배열에 저장
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

# 플로이드 워셜 알고리즘 이용, 두 노드가 이어져있는지 확인
for i in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][i]+graph[i][b])

# 하나의 노드에서 다른 노드로 화살표가 이어져있으면 두 노드 사이의 순서 비교가 가능함
# 모든 노드와 순서비교가 가능하면 순위를 알 수 있는 것.

answer = 0
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == n:
        answer += 1
    

print(answer)
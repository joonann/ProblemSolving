# 그래프 경로
# v개 이내의 노드 e 개의 간선

def DFS1(v):
    visited[v] = True
    for w in adj_v[v]:
        if visited[w] == False:
            DFS1(w)

t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())
    
    # 1 ~ v 까지 인접노드 행렬
    adj_v = [[]for _ in range(v+1)]

    # 입력을 받아 인접노드 행렬에 append
    for _ in range(e):
        a, b = map(int, input().split())
        adj_v[a].append(b)
    
    # s에서 g 갈 수 있는지
    s, g = map(int, input().split())

    # 방문 여부 배열
    visited = [False for _ in range(v+1)]
    stack = []
    DFS1(s)


    print(f'#{tc} {int(visited[g])}')


    

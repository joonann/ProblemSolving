# 노드의 거리
# SWEA 5102 난이도 D3

t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())   
    graph = [[] for _ in range(v+1)]
    visited = [0 for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    s, g = map(int, input().split())
    answer = 0

    q = [s]
    visited[s] = 1
    while q:
        now = q.pop(0) 
        if visited[g]:
            answer = visited[g] - 1
            break
        for next in graph[now]:
            if not visited[next]:
                visited[next] = visited[now] + 1
                q.append(next)
    print(f'#{tc} {answer}')
            
        



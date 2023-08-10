T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [False]*(V+1)
 
    for e in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
 
    S, G = map(int, input().split())
 
    def dfs(start, graph, visited, end):
        stack = [start]
        visited[start] = True
        while stack:
            value = stack.pop()
            if value == end:
                return 1
            if not visited[value]:
                visited[value] = True
            for j in graph[value]:
                if not visited[j]:
                    stack.append(j)
 
        return 0
 
    print(f'#{t}', dfs(S, graph, visited, G))

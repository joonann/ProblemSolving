# 길찾기
# SWEA 난이도 D4

# 0에서 99로 길 존재하는지
# stack dfs 로 구현해보자

def dfs(start, end, graph, visited):
    stack = [start]
    # visited[start] = True
    while stack:
        w = stack.pop()
        if w == end:
            return 1
        if visited[w] == False:
            visited[w] = True
            for i in graph[w]:
                if not visited[i]:
                    stack.append(i)
    return 0
        

# t = int(input())
t = 10
for tc in range(1, t+1):
    n, m = map(int, input().split())
    s = list(map(int, input().split()))

    graph = [[]for _ in range(100)]
    for i in range(m):
        a, b = s[i*2], s[i*2+1]
        graph[a].append(b)
    
    visited = [False for _ in range(100)]

    print(f'#{tc} {dfs(0, 99, graph, visited)}')
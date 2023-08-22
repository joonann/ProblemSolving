# contact
# SWEA D4

# 가장 나중에 연락받는 사람 중 번호가 가장 큰 사람

for tc in range(1, 11):
    answer = 0
    n, start = map(int, input().split())
    from_to = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    visited = [0 for _ in range(101)]
    for i in range(len(from_to)//2):
        a, b = from_to[2*i], from_to[2*i+1]
        graph[a].append(b)
    
    q = [start]
    visited[start] = 1
    distance = 1

    while q:
        now = q.pop(0)
        for next in graph[now]:
            if not visited[next]:
                visited[next] = visited[now] + 1
                q.append(next)
                distance = visited[next]
    for i in range(100, 0, -1):
        if visited[i] == distance:
            answer = i
            break


    print(f'#{tc} {answer}')
# subtree
# SWEA D2

t = int(input())
for tc in range(1, t+1):
    e, n = map(int, input().split())
    # n 부터 시작하는 이진트리
    l = list(map(int, input().split()))
    nodes = [0] * (e+2)
    graph = [[]for _ in range(e+2)]
    
    for i in range(e):
        a, b = l[2*i], l[2*i+1]
        graph[a].append(b)

    q = [n]
    nodes[n] = 1
    answer = 1
    while q:
        now = q.pop(0)
        for next in graph[now]:
            if not nodes[next]:
                nodes[next] = 1
                q.append(next)
                answer += 1

    print(f'#{tc} {answer}')
    

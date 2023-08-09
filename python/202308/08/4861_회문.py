# 회문
# SWEA
# 난이도 : D2

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    graph = [list(input()) for _ in range(n)]

    answer = [''] * m
    is_found = False

    for i in range(n):
        for j in range(n - m + 1):
            for k in range(m // 2 + 1):
                if graph[i][j+k] != graph[i][j+m-1-k]:
                    break
                answer[k] = answer[-1-k] = graph[i][j+k]
                if k == m // 2:
                    is_found = True
            if is_found:
                break
        if is_found:
            break

    if not is_found:
        for i in range(n-m+1):
            for j in range(n):
                for k in range(m // 2 + 1):
                    if graph[i+k][j] != graph[i+m-1-k][j]:
                        break
                    answer[k] = answer[-1-k] = graph[i+k][j]
                    if k == m // 2:
                        is_found = True
                if is_found:
                    break
            if is_found:
                break
    
    print(f'#{tc}', ''.join(answer))
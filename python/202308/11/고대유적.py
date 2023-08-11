# 고대 유적
# SWEA 난이도 D2

# 가장 긴 길이의 1 찾기
t = int(input())

for tc in range(1, t+1):
    
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    answer = 0
    for i in range(n):
        row_len = 0
        for j in range(m):
            if graph[i][j] == 0:
                answer = max(answer, row_len)
                row_len = 0
            else:
                row_len += 1
        answer = max(answer, row_len)

    for j in range(m):
        col_len = 0
        for i in range(n):
            if graph[i][j] == 0:
                answer = max(answer, col_len)
                col_len = 0
            else:
                col_len += 1
        answer = max(answer, col_len)
            


    print(f'#{tc} {answer}')


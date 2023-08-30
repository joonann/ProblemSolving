def perm(i, k):
    global ans
    global n
    if i == k:
        hx, hy = route[0]
        tmp = 0
        for i in range(1, n+2):
            nx, ny = route[i]
            tmp += abs(hx-nx)+abs(hy-ny)
            hx, hy = nx, ny
        if ans > tmp:
            ans = tmp
        return
    for j in range(i, k):
        route[j], route[i] = route[i], route[j]
        perm(i+1, k)
        route[j], route[i] = route[i], route[j]

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    route = [(arr[2*i], arr[2*i+1]) for i in range(2+n)]
    route[1], route[-1] = route[-1], route[1]
    ord = [i for i in range(n)]
    ans = int(10e9)
    perm(1, n+1)
    print(f'#{tc} {ans}')





def sol(i,s, level, visited):
    global answer
    if s > answer:
        return
    if level == n-2:
        if answer > s + mhtn[i][1]:
            answer = s + mhtn[i][1]
    else:
        for j in range(2,n):
            if not visited[j]:
                visited[j] = 1
                sol(j,s + mhtn[i][j], level+1, visited)
                visited[j] = 0
 
def manhattan(i,j):
    return abs(lst[i][0] - lst[j][0]) + abs(lst[i][1] - lst[j][1])
 
T = int(input())
for test_case in range(1, T + 1):
    n = int(input()) + 2
    lst = list(map(int, input().split()))
    lst = [(lst[2*i], lst[2*i+1]) for i in range(n)]
    mhtn = [[0]*n for _ in range(n)]
    for i in range(n-1):
        for j in range(i+1,n):
            mhtn[i][j] = manhattan(i,j)
            mhtn[j][i] = mhtn[i][j]
    # print(f'#{test_case} {lst}')
    visited = [0]*n
    answer = 2001
    sol(0,0,0,visited)
    print(f'#{test_case} {answer}')
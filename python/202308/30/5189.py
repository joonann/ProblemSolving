'''
전자카트
SWEA D3

'''



def perm(i, k):
    global ans
    if i == k:
        tmp = 0
        for j in range(n-1):
            tmp += graph[route[j]][route[j+1]]
        tmp += graph[route[n-1]][route[0]]
        if ans > tmp:
            ans = tmp
        return
    
    for x in range(i, k):
        route[i], route[x] = route[x], route[i]
        perm(i+1, k)
        route[i], route[x] = route[x], route[i]

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    route = [i for i in range(n)]
    ans = int(10e9)
    perm(1, n)
    
    print(f'#{tc} {ans}')
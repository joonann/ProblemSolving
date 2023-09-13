'''
퇴사
백준 14501

'''

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(1<<n):
    sub = []
    for j in range(n):
        if i & 1 << j:
            sub.append(j)
        
    prev = 0
    ben = 0
    is_not_possible = False
    # print('sub', sub)
    for a in sub:
        if prev > a:
            is_not_possible = True
            break
        prev = a + arr[a][0]
        # print('prev', prev)
        if prev > n:
            is_not_possible = True
            break
        ben += arr[a][1]
    
    if is_not_possible:
        continue
    # print(ben)
    if ans < ben:
        ans = ben

print(ans)
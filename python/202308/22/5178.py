# 노드의 합
# SWEA 5178
# 난이도 D2

t = int(input())
for tc in range(1, t+1):
    n, m, l = map(int, input().split())

    tree = [0] * (n+1)
    leaf = []

    for i in range(m):
        a, b = map(int, input().split())
        tree[a] = b
    
    print(tree)
    
    for i in range(n-m, 0, -1):
        tree[i] += tree[i*2]
        if i*2+1 <= n:
            tree[i] += tree[i*2 + 1]
    
    print(f'#{tc} {tree[l]}')

    
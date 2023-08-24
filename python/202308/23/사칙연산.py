# 사칙연산
# SWEA D4

for tc in range(1, 11):
    n = int(input())
    tree = [0] * (n+1)

    for _ in range(n):
        i = input().split()
        if i[1] not in '-+*/':
            i[1] = int(i[1])
        tree[int(i[0])] = i[1]
    
    for i in range(n, 0, -1):
        if tree[i] == '-':
            tree[i] = tree[i*2] - tree[i*2+1]
        elif tree[i] == '+':
            tree[i] = tree[i*2] + tree[i*2+1]
        elif tree[i] == '*':
            print('i', i, tree)
            print(tree[i*2], tree[i*2+1])
            tree[i] = tree[i*2] * tree[i*2+1]
        elif tree[i] == '/':
            tree[i] = tree[i*2] / tree[i*2+1]
    
    print(f'#{tc} {int(tree[1])}')
            

# 사칙연산
# SWEA D4

for tc in range(1, 11):
    n = int(input())
    tree = [0] * (n+1)
    arr = [list(input().split()) for _ in range(n)]

    for x in range(n-1, -1, -1):
        i = int(arr[x][0])
        if len(arr[x]) == 2:
            tree[i] = int(arr[x][1])
        if len(arr[x]) == 4:
            i2 = int(arr[x][2])
            i3 = int(arr[x][3])
            if arr[x][1] == '-':
                tree[i] = int(tree[i2]) - int(tree[i3])
            elif arr[x][1] == '+':
                tree[i] = int(tree[i2]) + int(tree[i3])
            elif arr[x][1] == '*':
                tree[i] = int(tree[i2]) * int(tree[i3])
            elif arr[x][1] == '/':
                tree[i] = int(tree[i2]) / int(tree[i3])
    print(f'#{tc} {int(tree[1])}')
            

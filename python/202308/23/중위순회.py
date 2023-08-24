# 중위순회
# SWEA D4

def in_order(i):
    global cnt
    global n

    if i <= n:
        in_order(2*i)
        answer[cnt]=  tree[i]
        cnt += 1
        in_order(2*i + 1)


for tc in range(1, 11):
    n = int(input())
    tree = [0] * (n+1)
    
    for _ in range(n):
        a = input().split()
        tree[int(a[0])] = a[1]
    
    answer = [0] * n
    cnt = 0

    in_order(1)

    print(f'#{tc}', ''.join(answer))


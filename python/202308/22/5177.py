# 이진 힙
# SWEA D3

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    tree = [0] + list(map(int, input().split()))
    for i in range(1, n+1):
        while i >= 2 and tree[i//2] > tree[i]:
            tree[i], tree[i//2] = tree[i//2], tree[i]
            i = i//2
    answer = 0
    while n > 0:
        n = n//2
        answer += tree[n]
    print(f'#{tc} {answer}')

    # 트리에 노드들을 추가하고 정렬해줌

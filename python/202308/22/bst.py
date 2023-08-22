# 이진탐색
# SWEA D2

# 1부터 n까지 자연수 이진탐색트리에 저장
# 배열에 저장은 중위순회 순서로 저장되어있고
# 전위순위 탐색 순서로 1, n//2 번째 요소 출력


# def tree(n):
#     global cnt
#     if n <= N:
#         tree(n*2)
#         bst[n] = cnt
#         cnt+=1
#         tree(n*2+1)

#       1
#    2     3
# 4   5   6  7
# 순서로 숫자를 배치해야됨
# 호출 순서
# {1{2{4{8[1삽입]9} [2삽입] 5{10 [3삽입] 11}} [4삽입] 
#    {3{6{12 [5삽입] 13} [6삽입] 7{14 [7삽입] 15}}}}}

def make_tree(a): # 중위 순회 이진트리 만들기
    global cnt

    if a <= n:
        make_tree(a*2)
        tree[a] = cnt
        cnt += 1
        make_tree(a*2 + 1)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    tree = [0 for _ in range(n+1)]
    cnt = 1

    make_tree(1)

    print(f'#{tc} {tree[1]} {tree[n//2]}')



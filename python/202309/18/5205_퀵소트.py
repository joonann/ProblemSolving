def qsort(A, l, r):
    if l < r:
        s = partition(A, l, r)
        print(A, 's', s, 'l r', l, r)
        qsort(A, l, s-1)
        qsort(A, s+1, r)

def partition(A, l, r):
    p = A[l]
    i = l
    j = r
    while i <= j:
        while i <= j and A[i] <= p:
            i += 1
        while i <= j and A[j] >= p:
            j -= 1
        


def partition(A, l, r):
    p = A[l]        # 가장 왼쪽 원소를 피봇으로 하는 경우
    i = l           # i는 오른쪽으로
    j = r           # j는 왼쪽으로 이동
    while i <= j:
        while i <= j and A[i] <= p:
            i += 1
        while i <= j and A[j] >= p:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[l],A[j] = A[j], A[l]
    return j
 

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    qsort(arr, 0, n-1)
    print(f'#{tc}', arr[n//2])



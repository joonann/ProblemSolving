def merge(l, mid, r):
    left = l        # 왼쪽 구간의 비교위치, l왼쪽 구간의 첫 원소 인덱스
    right = mid   # 오른쪽 구간의 비교위치, mid+1오른쪽 구간의 첫 원소 인덱스
    tidx = 0
    global cnt
    is_cnt = False
    if arr[mid-1] > arr[r]:
        is_cnt = True
    while left <= mid-1 or right <= r:        # 아직 남은 원소가 있으면
        if left <= mid-1 and right <= r:
            if arr[left] > arr[right]:
                tmp[tidx] = arr[right]
                right += 1
            else:
                tmp[tidx] = arr[left]
                left += 1
        elif left <= mid-1:
            tmp[tidx] = arr[left]
            left += 1
        else:
            tmp[tidx] = arr[right]
            right += 1
        tidx += 1
    for i in range(tidx):
        arr[l+i] = tmp[i]
    if is_cnt:
        cnt += 1
        
def merge_sort(l, r):
    if l == r:
        return
    mid = (l+r+1)//2
    merge_sort(l, mid-1)
    merge_sort(mid, r)
    merge(l, mid, r)
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    tmp = [0] * N
    cnt = 0
    merge_sort(0, N-1)
 
    print(f'#{tc}', arr[N//2], cnt)
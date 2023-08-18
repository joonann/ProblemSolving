# 암호생성기 
# SWEA 난이도 D3

t = 10

for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    m = min(arr) # 최솟값 구한다
    x = m // 15 # 최솟값에서 1, 2, 3, 4, 5 더한 15를 몇번 빼줄 수 있을까?
    for i in range(8):
        arr[i] = arr[i] - 15*(x-1) # 0이 되지 않게 x-1만큼 15 빼준거(반복 줄이기)
        
    is_end = False
    while not is_end:
        for i in range(1, 6):
            arr.append(arr.pop(0) - i)
            if arr[-1] <= 0:
                arr[-1] = 0
                print(f'#{tc}', *arr)
                is_end = True
                break

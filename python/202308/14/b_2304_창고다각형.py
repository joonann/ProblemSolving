# 창고다각형
# 백준 2304
# 실버 2

# n개의 막대 기둥
# 기둥을 이용한 창고
# 가장 작은 면적의 창고

# 기둥 개수
n = int(input())

columns = [list(map(int, input().split())) for _ in range(n)]
columns.sort(key=lambda x: x[0])

# 지붕 최대 높이
max_h = 0
for _, b in columns:
    max_h = max(max_h, b)
    
# 위치별 지붕의 높이구하기
now_h = columns[0][1]
for i in range(n):
    b = columns[i][1]
    if b == max_h:
        # 최대 높이 시작 지점
        start = i
        break
    columns[i][1] = max(now_h, b)
    now_h = columns[i][1]
now_h = columns[-1][1]
for i in range(n-1, -1, -1):
    b = columns[i][1]
    if b == max_h:
        end = i
        break
    columns[i][1] = max(now_h, b)
    now_h = columns[i][1]

# 오목한 지붕은 안되기 때문에
# 가장 높은 지붕 사이에 있는 기둥의 높이는 전부 max_h로 바꿔준다.
for i in range(n):
    if start < i < end:
        columns[i][1] = max_h

size = 0

fa, fb = columns[0][0], columns[0][1]
# 가장 높은 지붕이 나오기 전까지
for i in range(1, start+1):
    na, nb = columns[i][0], columns[i][1]
    size += (na - fa) * fb
    fa, fb = na, nb

# 가장 높은 지붕은 따로 추가해준다.
size += (columns[end][0] - columns[start][0] + 1) * max_h

fa = columns[end][0]+1
for i in range(end, n):
    na, nb = columns[i][0], columns[i][1]
    size += (na + 1 - fa) * nb
    fa = na + 1

print(size)
# 참외밭
# 백준 2477
# 난이도 : 실버2

# 참외 개수 구하기
# 1 m^2 참외개수 센 후 넓이 구하기
# 참외밭은 육각형(엔터키 모양)
# 왼쪽 위 꼭짓점에서 반시계방향으로 돌아서 둘레 구하기

# 1m^2 밭에 자라는 참외 개수
k = int(input()) 
lines = [list(map(int, input().split())) for _ in range(6)]

# 동서남북 1234
w, h, sw, sh = 0, 0, 1000, 1000
arr = [[]for _ in range(5)]

for d, l in lines:
    if d == 1 or d == 2:
        w = max(w, l)
    else:
        h = max(h, l)
    arr[d].append(l)

for d, l in lines:
    if arr[d].count() == 1:
        arr[0].append(0)
    else:
        arr[0].append(l)
for i in range(len(arr[0])):
    if arr[0][i] != 0




    



size = w*h - sw*sh
print(size*k)

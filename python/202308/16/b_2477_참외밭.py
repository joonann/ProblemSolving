# 참외밭
# 백준 2477
# 난이도 : 실버2

# 참외 개수 구하기
# 1 m^2 참외개수 센 후 넓이 구하기
# 참외밭은 육각형(엔터키 모양)
# 왼쪽 위 꼭짓점에서 반시계방향으로 돌아서 둘레 구하기

# 1m^2 밭에 자라는 참외 개수
# k = int(input()) 
# lines = [list(map(int, input().split())) for _ in range(6)]

# # 동서남북 1234
# w, h = 0, 0

# for i in range(len(lines)):
#     d = lines[i][0]
#     l = lines[i][1]
#     if d == 1 or d == 2:
#         w = max(w, l)
#     else:
#         h = max(h, l)

# for i in range(len(lines)):
#     l = lines[i][1]
#     if l == w:
#         m1 = i
#     if l == h:
#         m2 = i
# if m1 == m2 + 1:
#     m = m1
# elif m2 == m1 + 1:
#     m = m2
# else:
#     m = min(m1, m2)
# small = lines[(m+2)%6][1] * lines[(m+3)%6][1]

# size = w*h - small
# print(size*k)

# 동1서2남3북4 
s = [] # 방향, 거리 저장리스트  
x = [] # 가로 길이들 리스트
y = [] # 세로 길이들 리스트
low_num = [] # 작은 사각형의 가로 세로 길이

k = int(input())

for i in range(6):
    way, dist = map(int, input().split()) # 방향, 거리 입력
    s.append([way, dist])
    if s[i][0] == 3 or s[i][0] == 4: # 세로 저장
        x.append(s[i][1])
    if s[i][0] == 1 or s[i][0] == 2: # 가로 저장
        y.append(s[i][1])

# 작은 사각형의 길이 추출
for i in range(6):
    if s[i][0] == s[(i+2)%6][0]:
        low_num.append(s[(i+1)%6][1])

print(((max(x)*max(y)) - (low_num[0]*low_num[1]))*k)
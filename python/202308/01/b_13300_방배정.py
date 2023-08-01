# 방배정
# 백준 13300
# 난이도 : 브론즈 2

# 한 방에 한 명 배정도 가능
# 한 방에 최대 배정 인원 K
# 조건에 맞게 모든 학생을 배정하는 방의 최소 개수

n, k = map(int, input().split())
students = [[0, 0] for _ in range(7)]
rooms = 0
for _ in range(n):
    sex, grade = map(int, input().split())
    students[grade][sex] += 1

for i in range(1, 7):
    for j in (0, 1):
        rooms += students[i][j] // k
        if students[i][j] % k:
            rooms += 1
print(rooms)
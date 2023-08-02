# 색종이
# 백준 10163
# 난이도 브론즈 1

# n 개의 색종이
# 왼쪽 아래 (a, b) 너비c 높이 d 입력
# 색종이 별 보이는 부분의 면적

import sys
input = sys.stdin.readline

n = int(input())
graph = [[0 for _ in range(1001)] for _ in range(1001)]
counts = [0] * (n + 1)

# graph(맨 위에 놓인 종이 그래프)에 종이 한 장씩 덮어쓰기.
for paper in range(1, n + 1):
    a, b, c, d = map(int, input().split())
    for y in range(b, b+d):
        graph[y][a:(a + c)] = [paper] * c

for i in range(1, n + 1):
    result = 0
    for row in range(1001):
        result += graph[row].count(i)
    print(result)

# list를 한 번에 할당해주는 방식
# arr = [0, 0, 0, 0, 0]
# arr[1:3] = [1] * 2
# arr == [0, 1, 1, 0, 0]
# 으로 시간 줄이기

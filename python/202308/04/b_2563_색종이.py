# 색종이
# 난이도 : 실버 5

graph = [[0 for _ in range(100)] for _ in range(100)]
n = int(input()) # 색종이 장수
for _ in range(n): # 각 색종이의 맨 왼쪽 맨 아래 위치
    x, y = map(int, input().split())
    for i in range(x, x+10):
        graph[i][y:y+10] = [1] * 10

count = 0
for line in graph:
    count += line.count(1)
print(count)
'''
백준 17142 연구소3
난이도 : 골드 3

바이러스 M개 활성 상태로 모든 바이러스 활성화시키기

처음에는 모두 비활성 상태
활성 상태인 바이러스 > 인접한 모든 빈칸으로 동시 복제 1초 걸림
활성 바이러스가 비활성 바이러스로 가면 비활성 활성으로 바뀜

N x N 크기 정사각형 연구소
0 : 빈칸
1 : 벽
2 : 바이러스 위치

'''

# 바이러스 놓을 곳 정한다
# 시간을 구한다
# 최소인 경우를 출력한다
# 절대 안됨

# m개의 그룹으로 나눈다 (안 나눠지면 -1 출력)
# union, find 활용, union할 때마다 group_count 줄여서 m될 때까지
# 거리가 가까운 애들끼리 묶는다. 아파트 단지 

# m 개의 그룹에서 m개를 어떻게 정하지
# bfs로 방문한 숫자를 누적시키면서 그룹 내 바이러스 개수와 같은 바이러스 좌표는 그 그룹의 모든 바이러스를 최소의 시간을 들여 활성화시킬 수 있는 바이러스라는 뜻 : 
import sys
from collections import deque
import copy

input = sys.stdin.readline

# n, m 입력
n, m = map(int, input().split())
# 연구소 지도 입력
graph = [list(map(int, input().split())) for _ in range(n)]

all_infected_digit = 2**(m+2)-1
print(all_infected_digit)

time = [[0] * n for _ in range(n)]
for x in time:
	print(x)

# 바이러스 좌표
virus_coordinates = []
q = deque([])
virus_count = 0
virus_number = 1
for i in range(n):
	for j in range(n):
		if graph[i][j] == 2:
			virus_coordinates.append((i, j, virus_number))
			q.append([i, j, virus_number, 0]) # 좌표 (i, j)와 이 바이러스의 2진수 코드, 시간
			virus_count += 1
			virus_number <<= 1
		elif graph[i][j] == 1:
			graph[i][j] = -1

for i, j, virus_number, _ in q:
	graph[i][j] = virus_number

print(virus_coordinates)

for x in graph:
	print(x)

# # 그룹 수
# group_count = 0
# q = deque(virus_coordinates)
# while q:
	

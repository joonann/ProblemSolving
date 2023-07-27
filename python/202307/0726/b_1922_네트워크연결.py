# 네트워크 연결
# 백준 1922
# 난이도 : 골드 4

# 컴퓨터와 컴퓨터 연결
# 모든 컴퓨터 연결하는 최소 비용 출력
# 크루스칼 알고리즘 구현하기

import sys
import heapq

input = sys.stdin.readline

# 컴퓨터의 수 (노드)n
n = int(input())

# 연결할 수 있는 선의 수 (간선) m
m = int(input())

# union, find 함수를 위한 배열(연결된 최상위 노드 번호)
parent = [0] * (n + 1)
for i in range(n+1):
    parent[i] = i

# find 함수
def find(parent, x):
	if parent[x] != x:
		parent[x] = find(parent, parent[x])
	return parent[x]

# union 함수
def union(parent, x, y):
	a = find(parent, x)
	b = find(parent, y)
	if a < b:
		parent[b] = a
	else:
		parent[a] = b    

q = []
graph = [[] for _ in range(n + 1)]
connected = 1
total_cost = 0

for _ in range(m):
    a, b, cost = map(int,input().split())
    heapq.heappush(q, (cost, a, b))

while q:
	# n개의 컴퓨터가 모두 연결되어 있다면 반복문 탈출 
	if connected == n:
		break
	cost, a, b = heapq.heappop(q)

	# 사이클이 발생하지 않는 경우에만 union 후에 비용 추가해줌
	if find(parent, a) != find(parent, b):
		union(parent, a, b)
		total_cost += cost
		connected += 1

print(total_cost)
# 도시 분할 계획
# 백준 1647
# 난이도 : 골드4

# N개의 집, M개의 양방향 간선과 비용
# 2개의 최소신장트리 만들기
# 크루스칼 알고리즘 : 최소 비용을 더해가면서 사이클이 생기지만 않도록.
# union, find 함수를 정의한 이후, 알고리즘을 구현한다.

# find_parent 함수
import sys

input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x] 

# union 함수
def union_parent(x, y):
	a = find_parent(x)
	b = find_parent(y)

	if a < b:
		parent[b] = a
	else:
		parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n + 1)
for i in range(n + 1):
	parent[i] = i

# 간선과 비용 저장
edges = []
q = []
for _ in range(m):
	a, b, cost = map(int, input().split())
	edges.append((cost, a, b))

# 비용이 적은 순서대로 정렬
edges.sort(key=lambda x: x[0])  # 비용을 기준으로 간선 정렬하지 않고 heapq 최소힙을 사용했다.

# 출력할 총 비용
result = 0
# 마지막에 제거할 비용이 가장 큰 간선
last = 0
finished = 0
new_n = n - 1

# while q:
for cost, a, b in edges:
	# cost, a, b = heapq.heappop(q)
	if finished == new_n:
		break
	# 사이클이 발생하지 않는 경우 집합에 포함
	if find_parent(a) != find_parent(b):
		union_parent(a, b)
		result += cost
		last = cost
		finished += 1
	
print(result - last)

'''
1번부터 n번까지 도시와 m개의 단방향 도로 존재

'''

import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
roads = [[] for _ in range(n+1)]
distance = [1000001 for _ in range(n+1)]
answer = []
for _ in range(m):
	from_, to_ = map(int, input().split())
	roads[from_].append(to_)

q = deque([(x, 0)])
distance[x] = 0
while q:
	a, d = q.popleft()
	nd = d + 1
	for b in roads[a]:
		if distance[b] > nd:
			distance[b] = nd
			q.append((b, nd))

for c in range(1, n+1):
	if distance[c] == k:
		answer.append(c)

if answer:
	answer.sort()
	for a in answer:
		print(a)
else:
	print(-1)
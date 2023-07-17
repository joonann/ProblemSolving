import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
# 동서남북
dy = (0, 0, 1, -1)
dx = (1, -1, 0, 0)

# 첫 줄에 테스트케이스 T
T = int(input())

for _ in range(T):
	# n x n 크기
	n = int(input())	
    
	# 화성 지도( 각 칸의 비용 ) 입력
	marsMap = [list(map(int, input().split())) for _ in range(n)]
	
	# 각 칸까지 탐사하는 최단 비용 테이블
	costTable = [[INF for _ in range(n)] for _ in range(n)]

	# 다익스트라 알고리즘으로 최단경로 탐색
	q = []
	heapq.heappush(q, (marsMap[0][0], (0, 0)))
	while q:
		dist, now = heapq.heappop(q)
		for i in range(4):
			y = now[0]+dy[i]
			x = now[1]+dx[i]
			if (x >= 0 and x < n and y >= 0 and y < n):
				if costTable[y][x] < dist:
					continue
				cost = dist + marsMap[y][x]
				if cost < costTable[y][x]:
					costTable[y][x] = cost
					heapq.heappush(q, (cost, (y, x)))

	print(costTable[n-1][n-1])
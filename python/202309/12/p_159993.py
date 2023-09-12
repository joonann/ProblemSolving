from collections import deque

maps = ["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]

# 델타 
d = ((0, 1), (1, 0), (-1, 0), (0, -1))

def solution(maps):
	answer = 0
	
	n = len(maps)
	m = len(maps[0])
	visited = [[False] * m for _ in range(n)]
	q = deque()
	ans = -1

	# s 찾기
	is_s_found = False
	for i in range(n):
		for j in range(m):
			if maps[i][j] == 'S':
				# 시작점의 좌표와 현재 좌표에서의 비용 append해놓기
				q.append((i, j, 0))
				visited[i][j] = True
				# 2중 for문을 빠져나가기 위함
				is_s_found = True
				break

		if is_s_found:
			break
	
	# l을 찾기 위한 bfs
	is_l_found = False
	while q:
		x, y, c = q.popleft()

		if maps[x][y] == 'L':
			q = deque([(x, y, c)])
			visited = [[False] * m for _ in range(n)]
			visited[x][y] = True
			is_l_found = True
			break
		
		for a, b in d:
			nx, ny = x+a, y+b

			if 0<=nx<n and 0<=ny<m and \
				maps[nx][ny] != 'X' and not visited[nx][ny]:
				q.append((nx, ny, c+1))
				visited[nx][ny] = True

	if not is_l_found:
		return -1

	# 두번째 bfs
	while q:
		x, y, c = q.popleft()

		if maps[x][y] == 'E':
			ans = c
			break
			
		for a, b in d:
			nx, ny = x+a, y+b

			if 0<=nx<n and 0<=ny<m and \
				maps[nx][ny] != 'X' and not visited[nx][ny]:
				q.append((nx, ny, c+1))
				visited[nx][ny] = True

	return ans

print(solution(maps))
from collections import deque

q = deque()
nq = deque()

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def new_board_right(board, n):
	new = [[0] * n for _ in range(n)]
	for i in range(0, n, 1):
		q = deque()
		nq = deque()
		for j in range(n-1, -1, -1):
			num = board[i][j]
			if num:
				q.append(num)
		j = 0
		while j < len(q) - 1:
			num = q[j]
			if q[j] == q[j+1]:
				num *= 2
				j += 1
			nq.append(num)
			j += 1
		if j == len(q) - 1:
			nq.append(q[j])	
		print(nq)

		for j in range(n-1, -1, -1):
			if nq:
				new[i][j] = nq.popleft()
				continue
			break
	return new

for x in new_board_right(board, n):
	print(x)

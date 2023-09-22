'''
백준 12100
난이도 : 골드2
N x N 크기 보드에서 2048 게임 
최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록 출력
'''

from collections import deque

def new_board_up(board, n):
	# 1. q에 한 줄에 있는 숫자들(0 제외)를 차례로 넣어준다.
	# 2. q에 있는 숫자들 중에서 위쪽으로 옮겼을 때의 숫자들을 nq에 넣는다.
	# 3. nq에 있는 숫자들을 위에서부터 순서대로 적어준다.
	new = [[0] * n for _ in range(n)]
	for i in range(n):
		q = deque()
		nq = deque()
		for j in range(n):
			num = board[j][i]
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

		for j in range(n):
			if nq:
				new[j][i] = nq.popleft()
				continue
			break
	return new

def new_board_down(board, n):
	new = [[0] * n for _ in range(n)]
	for i in range(n-1, -1, -1):
		q = deque()
		nq = deque()
		for j in range(n-1, -1, -1):
			num = board[j][i]
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

		for j in range(n-1, -1, -1):
			if nq:
				new[j][i] = nq.popleft()
				continue
			break
	return new

def new_board_left(board, n):
	new = [[0] * n for _ in range(n)]
	for i in range(0, n, 1):
		q = deque()
		nq = deque()
		for j in range(0, n, 1):
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

		for j in range(0, n, 1):
			if nq:
				new[i][j] = nq.popleft()
				continue
			break
	return new
	
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

		for j in range(n-1, -1, -1):
			if nq:
				new[i][j] = nq.popleft()
				continue
			break
	return new

# board를 k회 이동해서 최댓값 반환하는 함수
def play_game(board, n, k):
	global ans
	if k == 0:
		tmp = max(map(max, board))
		ans = max(ans, tmp) 
		return
	play_game(new_board_up(board, n), n, k-1)
	play_game(new_board_down(board, n), n, k-1)
	play_game(new_board_left(board, n), n, k-1)
	play_game(new_board_right(board, n), n, k-1)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0
play_game(board, n, 5)
print(ans)


# 자물쇠와 열쇠
# n x n 자물쇠
# m x m 열쇠

# key[0] 1 2 3
# key[1] 4 5 6
# key[2] 7 8 9
# 뒤집어서 key[2], key[1], key[0]에서 요소 하나씩 엮어
# list로 만들면 90도 회전
def rotate_key(key):
	return list(zip(*key[::-1]))

# board의 중앙부분 전부 1이면 열쇠가 딱 맞는 것 >> True
def check_board(board, n, m):
	for i in range(n-1, n+m-1):
		for j in range(n-1, n+m-1):
			if board[i][j] != 1:
				return False
	return True

def attach_key(x, y, m, key, board):
	pass

def detach_key(x, y, m, key, board):
	pass

def solution(key, lock):
	m, n = len(key), len(lock)
	board_l = n * 2 + m - 2
	board = [[0 for _ in range(board_l)] for _ in range(board_l)]

	# [n-1:n+m-1] 가 가운데 자물쇠 범위
	for i in range(n):
		for j in range(n):
			board[i+n-1][j+n-1] = lock[i][j]
	
	rotated_key = key
	for _ in range(4):
		rotated_key = rotate_key(rotated_key)
		
		for x in range(n+m-1):
			for y in range(n+m-1):
				attach_key(x, y, m, rotated_key, board)
				if (check_board(board, n, m)):
					return True
				detach_key(x, y, m, rotated_key, board)  

return False
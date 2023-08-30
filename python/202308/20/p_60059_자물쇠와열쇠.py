def attach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] += key[i][j]

def detach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] -= key[i][j]

def rotate90(arr):
    n = len(arr)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n - i - 1] = arr[i][j]
    return result

def check(board, N):
    for i in range(N, N*2):
        for j in range(N, N*2):
            if board[i][j] != 1:
                return False
    return True

def solution(key, lock):
    M, N = len(key), len(lock)

    board = [[0 for _ in range(N*3)] for _ in range(N*3)]
    
	# 자물쇠 중앙 배치
    for i in range(N):
        for j in range(N):
            board[N+i][N+j] = lock[i][j]

    # 모든 방향
    for _ in range(4):
        key = rotate90(key)
        for x in range(1, N*2):
            for y in range(1, N*2):
                # 열쇠 넣기
                attach(x, y, M, key, board)
                # 열리는지 check
                if(check(board, N)):
                    return True
                # 열쇠 빼기
                detach(x, y, M, key, board)
                
    return False


# key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
# print(solution(key, lock))
'''
백준 13460
구슬탈출 2
난이도 : 골드 1

N x M 직사각형 보드
구멍 한 개
중력을 이용해서(왼/오른/위/아래 쪽으로 기울이기)
빨간 파란 구슬 하나 씩 넣고 
빨간 구슬을 구멍으로 빼는 게임
!!단, 파란 구슬이 구멍에 들어가면 안 됨

바깥 행 전부 막혀 있음
두 구슬은 동시에 같은 공간에 있을 수 없음
최소 몇 번 만에 성공하는지 구하는 프로그램
10번 이하로 움직여서 성공하지 못 하면 -1

'.' : 빈 칸
'#' : 벽
'O' : 구멍
'R' : 빨간 구슬
'B' : 파란 구슬

3 <= N, M <= 10

[입력 예시]
5 5
#####
#..B#
#.#.#
#RO.#
#####

[출력 예시]
1

'''
from collections import deque

# 입력값 받기
height, width = map(int, input().split())
board = [list(input()) for _ in range(height)]

# 왼쪽 오른쪽 위 아래
direction = ((0, -1), (0, 1), (-1, 0), (1, 0))

# 빨간 구슬, 파란 구슬, 구멍의 좌표 찾기
for i in range(n):
	for j in range(m):
		if board[i][j] == 'R':
			rx, ry = i, j
			board[i][j] = '.'
		elif board[i][j] == 'B':
			bx, by = i, j
			board[i][j] = '.'
		elif board[i][j] == 'O':
			hx, hy = i, j 
red_ball = [rx, ry]
blue_ball = [bx, by]
hole = [hx, hy]

# 기울인 횟수
min_lean_count = -1

q - 


print(min_lean_count)
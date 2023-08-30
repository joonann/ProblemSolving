'''
뱀 백준 3190 

Dummy도스게임 사과를 먹으면 길이 늘어남
자기 자신의 몸과 부딪히면 게임이 끝남

N x N 정사각 보드
보드 끝에는 벽
시작할 때는 1, 1에서 시작, 뱀의 길이 1
처음에는 오른쪽으로 움직임
뱀은 매 초 움직인다.

뱀의 이동
1. 몸 길이를 늘려 머리가 다음 칸으로 간다.
2. 이동한 칸에 사과가 있으면 그 칸에 있던 사과는 없어지고 꼬리는 움직이지 않는다.
3. 사과가 없으면 꼬리에 위치한 칸을 비워준다.

N : 보드의 크기
K : 사과의 개수 
K개 줄에 사과의 위치 (1, 1)에는 사과가 없음
L : 뱀의 방향 변환 횟수
L개 줄에 뱀의 방황 변환 정보, X초에 L/D 왼쪽/오른쪽으로 90도 방향회전
'''

# 우 하 좌 상 순서(시계방향)
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

n = int(input())
board = [[0 for _ in range(n+2)] for _ in range(n+2)]
k = int(input())

# 사과있는 곳 : -1로	
for _ in range(k):
	a, b = map(int, input().split())
	board[a][b] = -1

# 뱀의 머리 방향 ( d 인덱스 )
x = 0 
l = int(input())
m = []
for _ in range(l):
	sec, dir = input().split()
	if dir == 'D':
		x = (x + 1) % 4
	if dir == 'L':
		x = (x + 3) % 4
	m.append([int(sec), x])

# 뱀이 있는 곳 : 1
x = 0
second = 0
tail = [[1, 1]]
head = [1, 1]
board[1][1] = 1
i = 0

while True:
	second += 1

	head = [head[0]+d[x][0], head[1]+d[x][1]]
	hi, hj = head[0], head[1]
	# 벽이면 break
	if not(1<=hi<=n and 1<=hj<=n) or board[hi][hj] == 1:
		break

	tail.append([hi, hj])
	if board[hi][hj] == 0:
		a, b = tail.pop(0)
		board[a][b] = 0
	board[hi][hj] = 1

	if i < len(m) and second == m[i][0]:
		x = m[i][1]
		i += 1
		
print(second)
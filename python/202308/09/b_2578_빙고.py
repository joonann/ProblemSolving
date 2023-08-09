# 빙고
# 백준 2578
# 난이도 : 실버 4

# 1. 최소한 12개를 불러야한다.
# 2. (숫자, x좌표 y좌표, 빙고까지 남은 개수)
# 3. 빙고까지 남은 개수가 0이 되면 count += 1

# 입력 받아오기
graph = [list(map(int, input().split())) for _ in range(5)]
# bingo판 5x5
bingo = [[0 for _ in range(5)] for _ in range(5)]

data = []
for i in range(5):
    for j in range(5):
        data.append([graph[i][j], i, j, 5])

numbers = []
for _ in range(5):
    numbers.extend(list(map(int, input().split())))

turn = 0
left = 3
for number in numbers:
    turn += 1
    # number가 있는 data의 튜플 인덱스 찾기
    for index, item in enumerate(data):
        if item[0] == number:
            data_index = index
            break
    # number 의 좌표값 넣어주기
    ni, nj = data[data_index][1], data[data_index][2]
    bingo[ni][nj] = 1
    
    a = [0, 0, 0, 0] # 가로, 세로, 대각선
    # 가로 세로 확인
    for i in range(5):
        a[0] += bingo[ni][i]
        a[1] += bingo[i][nj]
    
    # 대각선
    if ni == nj:
        for i in range(5):
            a[2] += bingo[i][i]
    if ni + nj == 4:
        for i in range(5):
            a[3] += bingo[4-i][i]
    left -= a.count(5)

    if left <= 0:
        print(turn)
        break

    

    
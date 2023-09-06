'''
상어초등학교
백준 21608
골드 5

교실 n x n 
학교에 다닐 수 있는 학생은 n^2명 자리 정하는 날
학생 번호 1~n^2번
(r, c) r행 c열 (1, 1) ~ (n, n)

학생의 순서있음. 순서대로 자리 정하기

각 학생이 좋아하는 학생 4명 조사함
한 칸에 한 명만 앉을 수 있음
|r1-r2| + |c1-c2| = 1을 만족하는 두 칸(r1, c1)과 (r2, c2)를 인접하다고 한다.

1. 비어있는 칸 중 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
3. 2.를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로,
4. 3.을 만족하는 칸이 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정함.

만족도 출력
만족도 : 인접한 칸에 좋아하는 학생 수
0 >> 0
1 >> 1
2 >> 10
3 >> 100
4 >> 1000
'''

# s : 현재 자리를 찾고 있는 학생 번호
def find_seat(n, s, arr, seats, empty_spots):
    # 자리 행, 열, 좋아하는사람 수, 인접 빈 자리 개수
    like = [0, 0, 0, -1]
    # 자리 행, 열, 빈자리 개수
    empty = [0, 0, -1]
    is_like = False
    for i in range(1, n+1):
        for j in range(1, n+1):
            # 빈 자리라면
            likes = 0
            if seats[i][j] == 0:
                # 인접한 곳에 좋아하는 학생이 있는 자리가 있는지 확인
                for a, b in d:
                    ni, nj = i+a, j+b
                    if 1<=ni<=n and 1<=nj<=n and seats[ni][nj]:
                        if seats[ni][nj] in arr[s]:
                            likes += 1
                if likes:
                    if likes > like[2]:
                        like = [i, j, likes, empty_spots[i][j]]
                    elif likes == like[2] and empty_spots[i][j] > like[3]:
                        like = [i, j, likes, empty_spots[i][j]]
                    is_like = True
                
                # 좋아하는 학생이랑 인접한 자리가 없는 경우만 빈자리 개수 확인
                if not is_like:
                    if empty_spots[i][j] > empty[2]:
                        empty = [i, j, empty_spots[i][j]]
                        continue
                    if empty[2] == -1:
                        empty = [i, j, empty_spots[i][j]]
    if is_like:
        return like[0], like[1]
    return empty[0], empty[1]


d = ((1, 0), (0, 1), (-1, 0), (0, -1))
satisfaction_score = (0, 1, 10, 100, 1000)

n = int(input())
sc = n**2
# 학생이 좋아하는 학생들 리스트
arr = [[] for _ in range(sc+1)]
tmp = [list(map(int, input().split())) for _ in range(n**2)]

for s, s1, s2, s3, s4 in tmp:
    arr[s].append(s1)
    arr[s].append(s2)
    arr[s].append(s3)
    arr[s].append(s4)


seats = [[0]*(n+1) for _ in range(n+1)]

# 인접한 곳 빈칸 개수
empty_spots = [[4]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    empty_spots[i][1] -= 1
    empty_spots[1][i] -= 1
    empty_spots[i][n] -= 1
    empty_spots[n][i] -= 1

# 학생들의 만족도 단계(0~4)
satisfaction = [0]*(sc+1)

for ind in range(sc):
    # 학생 번호
    sn = tmp[ind][0]

    # 학생의 배치할 곳 찾기
    x, y = find_seat(n, sn, arr, seats, empty_spots)
    
    # 배치하기
    seats[x][y] = sn
    empty_spots[x][y] = 0

    # 학생들의 만족도를 증가시켜주는 반복문 sn, x, y 필요
    for a, b in d:
        nx, ny = x+a, y+b
        if 1<=nx<=n and 1<=ny<=n:
            if seats[nx][ny]:
                # 현재 배치한 학생의 만족도 높여주기
                if seats[nx][ny] in arr[sn]:
                    satisfaction[sn] += 1
                # 인접한 학생들의 만족도 높여주기
                if sn in arr[seats[nx][ny]]:
                    satisfaction[seats[nx][ny]] += 1
            else:
                # 인접한 곳의 empty_spots 낮춰주기
                empty_spots[nx][ny] -= 1

# 답안 출력
ans = 0
for s in satisfaction:
    ans += satisfaction_score[s]

print(ans)



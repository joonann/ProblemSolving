# 꽃길
# 백준 14620
# 난이도 : 실버 2

# 현재 땅에 심으면 드는 비용 테이블 구하기
# 심었을 때 인접한 13 개의 땅은 불가능 체크!
# dfs로 

# 점유된 땅 vec
occupied_d = ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1),\
                (-2, 0), (-1, 1), (0, 2), (1, 1), (2, 0), (1, -1), (0, -2))

# 비용 산출 vec
cost_d = ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1))

n = int(input())
yard = [list(map(int, input().split())) for _ in range(n)]

# 가격 테이블
#(1, 1) 부터 (n-2, n-2)까지만 사용
costs = [[0 for _ in range(n)] for _ in range(n)] 
for i in range(1, n-1):
    for j in range(1, n-1):
        for x, y in cost_d:
            costs[i][j] += yard[i+x][j+y]

# 점유된 땅인지 확인 (가장자리는 무조건 점유된 땅으로 설정)
occupied = [[False for _ in range(n)] for _ in range(n)]
# for i in range(n):
#     occupied[0][i] = True
#     occupied[n-1][i] = True
#     occupied[i][0] = True
#     occupied[i][n-1] = True
# # 안해도 될 것 같다.

# 최댓값은 3001보다 작음(200 * 15)
answer = 3001

def dfs(k, x, y):
    global answer
    
    if k == 0:
        answer = min(answer, now_cost)
    
stack 


print(answer)




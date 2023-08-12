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
# 0번째 occupied : 첫번째 선택 이후
# 1번째 occupied : 두번째 선택 이후
occupied = [[[False for _ in range(n)] for _ in range(n)] for _ in range(2)]

# 최댓값은 3001보다 작음(200 * 15)
answer = 3001


# 한 곳을 선택하고 occupied의 13 지점을 True로 바꿔준다.
# occupied에 false인 곳을 선택하고 13지점을 True로 바꿔준다.
# occupied가 3차원 배열이면 해결되겠다
# dfs가 끝나면 
def dfs(k, x, y, now_cost):
	# 이미 세 곳을 선택했으면 answer보다 작은지 확인한다.
	if k == 3:
		answer = min(answer, now_cost)
	now_cost += costs[x, y]
	k += 1
	
	
print(answer)




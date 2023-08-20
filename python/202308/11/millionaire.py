# 백만 장자 프로젝트
# SWEA 난이도 : D2

# 사재기 최대 이익
# 1. 연속 n일 물건 매매가 주어짐
# 2. 하루 최대 1 구입
# 3. 판매는 얼마든지

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    prices = list(map(int, input().split()))
	
    answer = 0
    total = 0
    sell_price = prices[-1]
	for i in range(n-1, -1, -1):
		buy_price = prices[i]
		if buy_price < sell_price:
			total += sell_price - buy_price
        else:
            sell_price = buy_price 
		answer = max(answer, total)

    print(f'#{tc} {answer}')
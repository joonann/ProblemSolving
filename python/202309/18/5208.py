'''
swea 5208 전기버스2
충전기 교환하는 방식의 전기버스

'''



t = int(input())
for tc in range(1, t+1):
	ans = 0
	# 1번 요소부터는 정류장의 배터리 용량
	battery = list(map(int, input().split()))
	n = battery[0]

	# 1번 요소부터 정류장에서 교체했을 때 갈 수 있는 최대 거리
	dp = [i+battery[i] for i in range(len(battery))]

	change_battery = 1
	how_far_can_i_go = dp[change_battery]
	while True:
		if n <= how_far_can_i_go:
			break
		max_charge = 0
		for i in range(change_battery, how_far_can_i_go + 1):
			if max_charge < dp[i]:
				change_battery = i
				how_far_can_i_go = dp[i]
				max_charge = how_far_can_i_go
		ans += 1
		
	print(f'#{tc}', ans)
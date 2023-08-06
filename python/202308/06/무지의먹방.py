# 무지의 먹방 라이브
# 2019 카카오 신입공채
# programmers 42891

# n 개의 음식

def solution(food_times, k):
	sum_times = 0
	next_food = []

	n = 0
	for food_time in food_times:
		sum_times += food_time
		next_food.append(n+1)
		n += 1

	next_food[n-1] = 0
	previous = n-1
	food = 0
	if sum_times <= k:
		return -1
	else:
		while k > 0:
			food_times[food] -= 1
			if food_times[food] == 0:
				next_food[previous] = next_food[food]
			else:
				previous = food
			food = next_food[food]
			k -= 1
	return food + 1
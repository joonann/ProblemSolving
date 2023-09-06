'''
별찍기
백준 2447
난이도 골드5
'''

def draw_stars(n):
	if n == 1:
		return ['*']
	
	stars = draw_stars(n//3)
	print('stars:', stars)
	L = []

	# 결국 stars에는 n//3 * n//3 크기의 별찍기 패턴이 들어감
	# 패턴 별로 8번 append, 가운데는 텅 빈 공간 append
	for star in stars:
		L.append(star*3)
	for star in stars:
		L.append(star + ' '*(n//3) + star)
	for star in stars:
		L. append(star*3)
	return L

n = int(input())

print('\n'.join(draw_stars(n)))

# for i in range(n):
# 	print(draw_stars(n)[i])
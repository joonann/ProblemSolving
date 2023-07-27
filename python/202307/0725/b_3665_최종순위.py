# 최종 순위
# 백준 3665
# 난이도 : 골드 1

# T 테스트 케이스
# n 팀 개수
# 작년 팀 순위(1등부터)
# m 개의 작년과 상대적인 등수가 바뀐 쌍의 수
# 등수 바뀐 두 팀

# 1. 올해 순위 출력
# 2. 확실한 순위를 찾을 수 없으면 ? 출력
# 3. 순위를 정할 수 없는 경우 'IMPOSSIBLE'

import sys

input = sys.stdin.readline
T = int(input())

def print_list(list1):
	for a in list1:
		print(a, end=' ')

for _ in range(T):
	# 테스트 케이스별 변수 입력
	n = int(input())
	last_year_rank = list(map(int, input().split()))
	m = int(input())

	# 순위가 바뀐 경우들 담는 리스트
	changed_rank = []
	for _ in range(m):
		changed_rank.append(tuple(map(int, input().split())))

	# 바뀐 순위가 없는 경우 작년 순위 그대로 출력
	if m == 0:
		print_list(last_year_rank)
		continue

	# 인접한 작년 순위 



	



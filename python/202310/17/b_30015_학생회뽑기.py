'''
학생회 뽑기
백준 골드 3

n명 중 
k명을 뽑아 학생회 구성 

n명의 능력 (1번~n번) 점수
를 2진수로 나타내고
& 연산으로 전체 학생회의 능력값을 구할 수 있음
능력값의 최댓값 출력

'''

from itertools import combinations

n, k = map(int, input().split())
ability = list(map(int, input().split()))

max_a = 0
is_k = False

bin = 2**19
print(bin)
while bin >= 1:
	temp = []
	for a in ability:
		if a & bin:
			temp.append(a)
	if len(temp) > k:
		ability = temp
	elif len(temp) == k:
		ability = temp
		is_k = True
		break
	bin //= 2

print(ability)
# 0 ~ N 번 학생 / N+1 개의 팀 존재

# 0 : 팀 합치기 연산 : union 연산
# 1 : 같은 팀 여부 확인 연산 : find 연산
# M 개의 팀 합치기 (0 a b) / 같은 팀 여부 확인 (1 a b)
# 같은 팀 여부 확인 (1 a b)의 결과 출력 'YES' / 'NO'

n, m = map(int, input().split())

# n+1 명의 학생
team = [0 for _ in range(n + 2)]

# 팀 합치기 이전, i 번 학생은 i 번 팀
for i in range(1, n + 2):
	team[i] = i

# 팀 찾기 연산 구현 : a의 팀 번호를 거슬러 올라가서 팀 확인
def find_team(a):
	if team[a] != a:
		team[a] = find_team(team[a])
	return team[a]

# 팀 합치기 연산 구현 : a의 팀과 b의 팀 찾아서
def union_team(a, b):
	a = find_team(a)
	b = find_team(b)
	if a < b:
		team[b] = a
	else:
		team[a] = b


for _ in range(m):
	x, a, b = map(int, input().split())
	if x == 1:
		union_team(a, b)
	else:
		if find_team(a) == find_team(b):
			print('YES')
		else:
			print('NO')


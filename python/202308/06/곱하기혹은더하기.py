# 각 자리가 숫자로만 이루어진 문자열

from collections import deque

# x나 +를 넣어서 왼쪽부터 연산했을 때 가장 큰 수 출력
# 그리디 알고리즘을 이용해 그 순간 x나 + 중 큰 경우로 선택

n = deque(list(map(int, input())))
a = n.popleft()
while n:
	b = n.popleft()
	a = max(a+b,a*b)
print(a)
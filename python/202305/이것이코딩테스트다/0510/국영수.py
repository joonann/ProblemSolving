
# < 람다식 >
# 람다식은 익명함수 표현하는 식  
# 아래 두 식은 같은 것.
# def f(x, y): return x+y
# f = lambda x, y: x+y
# ans = f(1, 2)
# print(ans) 
# # >> 3 출력

# 람다식을 이용해 위치를 바꾼 새로운 리스트를 반환해 newl에 저장해줄 수 있다. 
# l = [1, 2, 3, 4]
# f = lambda x : [x[1], x[0], x[3], x[2]]
# newl = f(l)
# print(newl)
# # >> [2, 1, 4, 3]

# < sorted 메서드 >
# 매개변수에 iterable(반복가능한) 데이터 넣어주면 정렬한다. (기본이 오름차순 정렬)
# l = ['czz', 'azz', 'bzz']
# newl = sorted(l)
# print(newl)
# # >> ['azz', 'bzz', 'czz']

# 매개변수에 list의 list인 경우 첫 번째 요소를 기준으로 정렬한다.
# l = [[2, 'czz'], [1, 'azz'], [1, 'bzz'], [2, 'bzz'], [3, 'azz']]
# f = lambda x : [x[0], x[1]]
# newl = sorted(l, key=f)
# print(newl)
# # >> [[1, 'azz'], [1, 'bzz'], [2, 'bzz'], [2, 'czz'], [3, 'azz']]

# 매개변수에 key=func 추가해 정렬하는 기준을 바꿀 수 있다.
# l = [[2, 'czz'], [4, 'azz'], [1, 'bzz'], [2, 'bzz'], [3, 'azz']]
# f = lambda x: x[1]
# newl = sorted(l, key=f)
# print(newl)
# # > [[4, 'azz'], [3, 'azz'], [1, 'bzz'], [2, 'bzz'], [2, 'czz']]

# sorted를 이용해 내림차순으로 정렬하는 방법
# lambda의 반환값이 int인 경우 앞에 -를 붙여서 음수로 비교하기
# reverse= 값 설정해주기
# l = [[2, 'czz'], [1, 'azz'], [1, 'bzz'], [2, 'bzz'], [3, 'azz']]
# f = lambda x : -x[0]  
# newl = sorted(l, key=f) 
# newl = sorted(l, reverse=True)
# newl = sorted(l, key=f, reverse=False)
# print(newl)
# # >> [[3, 'azz'], [2, 'czz'], [2, 'bzz'], [1, 'azz'], [1, 'bzz']]

'''
sort() 와 sorted() 의 차이
a.sort()는 a를 정렬
sorted(a)는 a를 복사해서 정렬 후 반환 
'''

n = int(input())
l = []
for _ in range(n):
	a, b, c, d = input().split()
	nb, nc, nd = map(int, [b, c, d])
	l.append([a, nb, nc, nd])

newl = sorted(l, key=lambda x: ([-x[1], x[2], -x[3], x[0]]))

for i in range(n):
	print(newl[i][0])


''' 입력 예시
8
d 1 1 2
c 3 2 3
e 2 3 2
g 2 2 1
b 2 2 1
f 3 1 1
h 1 1 3
a 1 2 3

정렬 후

f 3 1 1
c 3 2 3
b 2 2 1
g 2 2 1
e 2 3 2
h 1 1 3
d 1 1 2
a 1 2 3

'''
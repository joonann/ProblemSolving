# 럭키 스트레이트
# 백준 18406
# 난이도 : 브론즈 2

# 점수가 특정 조건
# 점수 N 자릿수 절반 왼쪽과 오른쪽
# 각 자릿수의 합을 더한 값이 동일해야 됨
# 조건 만족하면 LUCKY / 만족하지 않으면 READY 출력

n = list(map(int, input()))
a, b = 0, 0
l = len(n)//2
for i in range(l):
    a += n[i]
    b += n[i+l]
if a == b:
	print('LUCKY')
else:
      print('READY')
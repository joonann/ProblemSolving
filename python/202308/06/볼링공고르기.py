# 볼링공 고르기
# A, B 서로 다른 무게 고르기
# n개의 볼링공 m : 볼링공 무게 최댓값 

n, m = map(int, input().split())
weights = list(map(int, input().split()))
counts = [0] * (m+1)
for weight in weights:
    counts[weight] += 1
answer = 0

# 거꾸로 누적합
for i in range(len(counts) - 1, 0, -1):
    counts[i-1] += counts[i]
print(counts)

for i in range(1, len(counts)-1):
	now = counts[i] - counts[i+1]
	if counts[i+1] < counts[i]:
		answer += now * counts[i+1]
print(answer)
 
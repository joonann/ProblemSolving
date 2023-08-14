# 수열
# 백준 2559
# 난이도 : 실버 3

n, k = map(int, input().split())
t = [0]+list(map(int, input().split()))
# 누적합으로 구한다.
for i in range(1, n+1):
    t[i] = t[i-1]+t[i]
answer = -10000001

for a in range(k, n+1):
    answer = max(answer, t[a] - t[a-k])
print(answer)
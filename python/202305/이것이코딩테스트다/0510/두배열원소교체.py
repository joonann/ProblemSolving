n, k = map(int, input().split())
sum = 0
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)	

for i in range(n):
	sum += (B[i] if i < k else A[i])
print(sum)


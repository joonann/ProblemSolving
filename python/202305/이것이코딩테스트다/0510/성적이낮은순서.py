n = int(input())
l = []
for _ in range(n):
	a, b = input().split()
	l.append([a, int(b)])
newl = sorted(l, key=lambda x: x[1])	

for a in newl:
	print(a[0], end=" ")
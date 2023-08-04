# 종이 자르기
# 백준 2628
# 난이도 실버5

n, m = map(int, input().split())
papers = int(input())
slice_i = [0]
slice_j = [0]
# 가로로 자르기, 세로로 자르기 모아놓기
for _ in range(papers):
    a, b = map(int, input().split())
    if a == 0 :
        slice_j.append(b)
    else:
        slice_i.append(b)
slice_i.append(n)
slice_j.append(m)
slice_i.sort()
slice_j.sort()

width = 0
height = 0
for i in range(len(slice_i)-1):
    width = max(width, slice_i[i+1]-slice_i[i])

for j in range(len(slice_j)-1):
    height = max(height, slice_j[j+1]-slice_j[j])
print(width * height)

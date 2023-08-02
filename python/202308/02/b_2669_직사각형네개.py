# 직사각형 네개의 합집합의 면적 구하기
# 백준 2669 
# 난이도 실버 5

boxes = [list(map(int, input().split())) for _ in range(4)]

map = [[False for _ in range(100)] for _ in range(100)]

count = 0
for a, b, c, d in boxes:
    for i in range(a, c):
        for j in range(b, d):
            if map[i][j] == False:
                map[i][j] = True
                count += 1
            
print(count)
'''
n x n 크기 도시
각 칸이 빈칸/치킨집/집 중 하나
도시의 치킨거리  = 가까운 치킨거리의 합
'''

from itertools import combinations

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
result = int(10e9)
house = [] 
chick = [] 

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chick.append([i, j])

for chi in combinations(chick, m): 
    temp = 0  
    for h in house: 
        chi_len = 999 
        for j in range(m):
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        temp += chi_len
    result = min(result, temp)

print(result)
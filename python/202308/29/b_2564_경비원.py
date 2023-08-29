'''
경비원
백준 2564
실버 1

첫째줄에 가로, 세로 길이
상점 개수
상점있는 변, 위치(왼쪽/위 부터)
 1
3 4
 2
 
1 북쪽 2 남쪽 3 서쪽 4 동쪽
동근이 있는 변, 위치

'''

# a oa
# b ob


# i j 1    2      3     4
# 1 x      x     a+b   oa+b
# 2 x      x     a+ob  oa+ob
# 3 a+b   oa+b    x     x    
# 4 a+ob  oa+ob   x     x

# j 13 >> a   24 >> oa
# i 13 >> b   24 >> ob

# x=[0, a, oa, a, oa] j접근
# y=[0, b, ob, b, ob] i접근


w, h = map(int, input().split())
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
i, a = map(int, input().split())

top = [1, 2]
side = [3, 4]
now_line = [0, w, w, h, h]
side_line = [0, h, h, w, w]

ans = 0
sl = side_line[i]
nl = now_line[i]
for j, b in s:
    if i == j:
        ans += abs(b-a)
    elif (i in top and j in top) or (i in side and j in side):
        ans += min(sl + a+b, sl + nl-a + nl-b)
    else:
        oa = nl - a
        ob = sl - b
        x = [0, a, oa, a, oa]
        y = [0, b, ob, b, ob]
        ans += x[j]+y[i]
print(ans)        

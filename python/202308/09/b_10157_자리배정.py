# 자리 배정
# 백준 10157
# 난이도 : 실버 4

# 공연장 가로 C개 세로 R개 좌석x in C / y in R
# 

# 첫번째 껍질 : 1, 1에서 시작 c*2 + (r-2)*2 만큼
# 두번째 껍질 : 2, 2에서 시작 (c-2)*2 + (r-4)*2
# 세번째 껍질 : 3, 3에서 시작 (c-4)*2 + (r-6)*2

# n번째 껍질 : n, n에서 시작 (c-2*(n-1))*2 + (r-2*n)*2
#                           = 2c + 2r - 8n + 4
#                           = 2(c + r - 4n + 2)

# 현재 껍질에서 가로 : c - 2(n-1)   세로 : r - 2(n-1)

# 몇 번째 껍질 안에 있는지

c, r = map(int, input().split())
k = int(input())

if k > c*r:
    print(0)
else:
    n = 1
    shell = 0

    while True:
        shell += 2*(c+r-4*n+2)
        if k > shell:
            k -= shell
            n+= 1
            continue
        x = n + k // 
        y = n
        break
    print(x, y)

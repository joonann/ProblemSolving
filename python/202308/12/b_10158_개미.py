# 개미
# 백준 10158
# 난이도 : 실버 4

# 가로 w 세로 h
# 개미는 대각선으로 움직임

w, h = map(int, input().split())
x, y = map(int, input().split())
t = int(input())

nx = x + t % (w*2)
ny = y + t % (h*2)

if nx > w:
    nx = w - (nx - w)
if ny > h:
    ny = h - (ny - h)
if nx < 0:
    nx *= -1
if ny < 0:
    ny *= -1

print(nx, ny)
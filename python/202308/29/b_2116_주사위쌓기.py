'''
주사위 쌓기
1~6 주사위(but 마주보는 면 합이 항상 7은 아님)

주사위 순서대로 쌓기
1. 윗면에 적힌 숫자는 아랫면 숫자와 같아야 한다.
2. 

n 주사위 개수
주사위별 숫자 A B C D E F
  A
B C D E
  F

A - F
B - D
C - E
'''
opp = [5, 3, 4, 1, 2, 0]
n = int(input())
dice = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(6):
    down = i
    up = opp[down]
    dice_sum = 0
    for j in range(6):
        if j == down or j == up:
            continue
        if dice_sum < dice[0][j]:
            dice_sum = dice[0][j]
    for i in range(1, n):
        down = dice[i].index(dice[i-1][up])
        up = opp[down]
        tmp = 0
        for j in range(6):
            if j == down or j == up:
                continue
            if tmp < dice[i][j]:
                tmp = dice[i][j]
        dice_sum += tmp
    if ans < dice_sum:
        ans = dice_sum
print(ans)


                
        


'''
컨베이어 벨트 위의 로봇
몇번째 단계가 진행중일 때 종료되었는지 출력

길이 n인 컨베이어 벨트(길이 2n인 벨트가 감싸고 돌고 있음)
1~2n까지의 칸이 있음
한칸씩 회전

1번 칸이 있는 위치 : 올리는 위치
n번 칸이 있는 위치 : 내리는 위치

로봇을 '올리는 위치'에 하나씩 올릴 수 있음
로봇이 올라가거나 이동하면 그 칸의 내구도 1 감소

1. 벨트가 회전
2. 로봇이 한칸씩 이동(이동할 수 없으면 가만히 있음)
    이동하기 위해서는 다음 칸에 로봇이 없고, 내구도가 1이상 남아있어야 됨
3. 올리는 위치에 내구도가 0이 아니면 로봇을 올린다.

내구도가 0인 칸이 k개가 되면 과정 종료
종료되었을 때 몇번째 단계가 

a는 1번째부터 2n번째까지 칸의 내구도
'''

# 벨트가 한칸 회전
def rotate_belt():
    down.append(up.pop())
    up.insert(0, down.pop(0))
    robots.pop()
    robots.insert(0, 0)

# 로봇 올리고 올리는 위치 내구도 낮추기
def add_robot():
    global zeros
    if up[0] >= 1:
        robots[0] = 1
        up[0] -= 1
        if up[0] == 0:
            zeros += 1

def move_robot(robot_loc, n):
    global zeros
    new_loc = robot_loc + 1
    if robot_loc == n-1:
        robots[n-1] = 0
    elif robots[new_loc] == 0 and up[new_loc] >= 1:
        robots[robot_loc] = 0
        robots[new_loc] = 1
        up[new_loc] -= 1
        if up[new_loc] == 0:
            zeros += 1
    
n, k = map(int, input().split())
a = list(map(int, input().split()))
up, down = a[:n], a[-1:n-1:-1]
robots = [0]*n
step, zeros = 0, 0
while True:
    step += 1
    rotate_belt()
    for i in range(n-1, -1, -1):
        if robots[i]:
            move_robot(i, n)
    add_robot()
    if zeros >= k:
        break

print(step)

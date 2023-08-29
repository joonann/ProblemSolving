'''
톱니바퀴
백준 14891
난이도 골드5

4개(1, 2, 3, 4번)의 톱니바퀴(8개 톱니)
N극/S극
톱니바퀴를 K번 회전(시계/반시계)
인접한 톱니바퀴와 만나는 톱니가 
1. 같은 극이면 회전하지 않는다.
2. 다른 극이면 반대방향으로 회전한다.

'''
s = [[], [7, 0, -1], [0, 7, 1]]

def rotate(gear, s_d):
    start, end, step = s_d
    for i in range(start, end, step):
        tmp = gear[i+step]
        gear[i+step] = gear[i] 
    gear[end] = tmp    

gear = [[]]+[list(map(int, input())) for _ in range(4)]
k = int(input())
for _ in range(k):
    gear_num, d = map(int, input().split())
    
for g in gear:
    print(g)
rotate(gear[1], s[-1])

for g in gear:
    print(g)

# answer = 0
# for i in range(4):
#     if gear[i][0] == S:
#         answer += 1<<i


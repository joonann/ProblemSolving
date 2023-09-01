def rotate(num, direct):
    if not visited[num]:
        visited[num] = True
        rotate_list[num] = direct

    if num == 0:
        if wheel[num][2] != wheel[num+1][-2]:
            if not visited[num+1]:
                rotate(num+1, -direct)
    elif num == 3:
        if wheel[num][-2] != wheel[num-1][2]:
            if not visited[num-1]:
                rotate(num-1, -direct)
    else:
        if wheel[num][-2] != wheel[num-1][2]:
            if not visited[num-1]:
                rotate(num-1, -direct)
        if wheel[num][2] != wheel[num+1][-2]:
            if not visited[num+1]:
                rotate(num+1, -direct)
        

def rotate_go(num):
    wheel[num].append(wheel[num].pop(0))

def rotate_back(num):
    wheel[num].insert(0, wheel[num].pop())

wheel = []
for i in range(4):
    chk = []
    for j in input():
        chk.append(j)
    wheel.append(chk)

K = int(input())
for k in range(K):
    visited = [False]*4
    rotate_list = [0, 0, 0, 0]
    rotate_wheel, direct = map(int, input().split())
    rotate(rotate_wheel-1, direct)
    
    func_list = [None, rotate_back, rotate_go]
    for w in range(4):
        if rotate_list[w] == 1:
            rotate_back(w)
        elif rotate_list[w] == -1:
            rotate_go(w)
        else:
            continue

result = 0
for w in range(4):
    if wheel[w][0] == '1':
        result += 2**w

print(result)
 
def dfs(idx, cnt):
    global result
 
    if cnt == change:
        chk = ''
        for n in num_list:
            chk += n
        if result < int(chk):
            result = int(chk)
        return
 
    for i in range(idx, len(num)):
        for j in range(i+1, len(num)):
            if int(num_list[i]) <= int(num_list[j]):
                num_list[i], num_list[j] = num_list[j], num_list[i]
                dfs(i, cnt+1)
                num_list[i], num_list[j] = num_list[j], num_list[i]
 
    if result == 0 and cnt < change:
        if (change - cnt) % 2 == 1:
            num_list[-1], num_list[-2] = num_list[-2], num_list[-1]
        dfs(idx, change)
 
 
T = int(input())
for t in range(1, T+1):
    num, change = input().split()
    num_list = [n for n in num]
    change = int(change)
    result = 0
    dfs(0, 0)
    print(f'#{t} {result}')
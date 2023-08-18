# 피자 굽기
# SWEA 난이도 D2

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    # [피자번호, 녹아야할치즈] 자료구조 사용
    c = [[i+1, c[i]] for i in range(m)]


    q = [] # 화덕
    for _ in range(n): # 화덕에 n개만큼 피자 넣기
        q.append(c.pop(0))
    while True:
        if len(q) == 1: # 하나 남으면 결과 출력
            print(f'#{tc} {q.pop()[0]}')
            break
        now = q.pop(0)
        now[1] = now[1] // 2
        if now[1] == 0: # 치즈가 0이면
            if c: # 남은 피자 있는지 확인해서
                q.append(c.pop(0)) # 남은피자 화덕 빈자리에 채우기
        else:
            q.append(now) # 치즈가 0이 아니면 다시 넣기

        


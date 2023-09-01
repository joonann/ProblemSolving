def f(k, N):
    global max_v
    if k == N:
        money = int(''.join(map(str, card)))
        if max_v < money:
            # print('이번 바꾸기를 통해 최댓값이 바뀌었다.', money)
            max_v = money
        # else:
        #     print('바꿨지만 최댓값 그대로', money)
    else:
        for i in range(len(card)):
            for j in range(i + 1, len(card)):
                card[i], card[j] = card[j], card[i]
                m = int(''.join(map(str, card))) 
                if m not in memo[k]:
                    # print(k+1, '번째에 ', m, '은 처음 나오니까 다음')
                    memo[k].append(m)
                    f(k + 1, N)
                card[i], card[j] = card[j], card[i]
 
 
T = int(input())
for tc in range(1, T + 1):
    num, N = input().split()
    card = list(map(int, num))
    N = int(N)
    max_v = 0
    memo = [[] for _ in range(N)]

    f(0, N) 
    print(f'#{tc} {max_v}')

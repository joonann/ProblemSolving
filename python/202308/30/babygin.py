def baby_gin(p):
    r = tri = 0
    if p[0] == p[1] == p[2]:
        tri += 1
    if p[3] == p[4] == p[5]:
        tri += 1
    if p[0]+2 == p[1] +1 == p[2]:
        r += 1
    if p[3] + 2 == p[4] + 1 == p[5]:
        r += 1
    if r + tri == 2:
        return 1
    else:
        return 0


def nPk(i, N, p):
    global ans
    if i == N:
        if baby_gin(card):
            ans = 'Baby Gin'
            return 1
    else:
        for j in range(i, N):
            card[i], card[j] = card[j], card[i]
            if nPk(i+1, N, p):
                return 1
            card[i], card[j] = card[j], card[i]



T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input()))
    ans = 'Lose'
    nPk(0, 6, card)
    print(f'#{tc} {ans}')
# 쇠막대기 자르기
# SWEA 난이도 : D4

# 쇠막대기 절단
# 현재 층수를 구하고
# 레이저 나올 때마다 total에 더해주는 방식

t = int(input())

for tc in range(1, t+1):
    s = input()
    answer = 0
    floor1 = 0
    for i in range(len(s)):
        if s[i] == '(':
            floor1 += 1
        else:
            floor1 -= 1
            if s[i-1] == '(':
                answer += floor1
            else:
                answer += 1

    print(f'#{tc} {answer}')
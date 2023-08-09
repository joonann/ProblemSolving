# 스위치 켜고 끄기
# 백준 1244
# 난이도 : 실버 4

# 1부터 연속적인 번호의 스위치
# '1' 켜져있음 / '0' 꺼져있음
# 남학생 : 스위치 번호가 자신의 숫자의 배수이면 상태 바꿈 
# 여학생 : 자신의 숫자 기준 대칭인 번호의 스위치 상태가 같은 최대 범위의 스위치를 모두 바꿈
# ex ) 1 1 1 0 0(기준) 0 1 0 1 >> 10001 다섯개 바꿈


n = int(input())
switch = list(map(int, input().split()))
m = int(input())
for i in range(m):
    MF, number = map(int, input().split())
    number -= 1
    if MF == 1:
        for j in range(number, n, number+1):
            switch[j] ^= 1
    else:
        switch[number] ^= 1
        for j in range(1, n//2+1):
            if number + j >= n or number - j < 0:
                break
            if switch[number + j] != switch[number - j]:
                break
            if switch[number + j] == switch[number - j]:
                switch[number + j] ^= 1
                switch[number - j] ^= 1
for i in range(n):
    if i > 0 and i % 20 == 0:
        print()
    print(switch[i], end=' ')

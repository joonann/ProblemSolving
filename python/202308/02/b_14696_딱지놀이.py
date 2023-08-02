# 딱지놀이
# 백준 14696
# 난이도 : 브론즈 1

# A, B의 딱지 별(4) 동그라미(3) 네모(2) 세모(1)
# 별 > 동그라미 > 네모 > 세모 순으로 많은 쪽이 이김

n = int(input())
for _ in range(n):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.pop(0)
    B.pop(0)
    result = 'D'
    for i in range(4, 0, -1):
        A_count = A.count(i)
        B_count = B.count(i)
        if A_count > B_count:
            result = 'A'
            break
        elif A_count < B_count:
            result = 'B'
            break
    print(result)    
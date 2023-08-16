# 토너먼트 카드게임
# SWEA 난이도 D2

# 가위바위보
# 1번부터 n명까지 학생
# 가위1 바위2 보3 

# 가위바위보 승자 알려주는 함수

def winner(rsp, i, j):
    check = (rsp[j] + 3 - rsp[i]) % 3
    if check == 1:
        return j
    elif check == 2:
        return i
    else:
        return i
        
def divide(rsp, i, j):
    if i == j:
        return i
    if j - i == 1:
        return winner(rsp, i, j)
    return winner(rsp, divide(rsp, i, (i+j)//2), divide(rsp, (i+j)//2+1, j))

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    rsp = [0] + list(map(int, input().split()))
    answer = divide(rsp, 1, n)
    
    print(f'#{tc} {answer}')
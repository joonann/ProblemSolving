'''
암호코드스캔
8개 숫자(7자리 상품고유번호 + 1자리 검증코드)
(홀수 자리의 합*3)+(짝수자리의 합)+(검증코드)가 10의 배수가 돼야됨
이 방식으로 검증코드를 정한다.

암호 코드 스캐너  개발하기
1. 세로 2000 가로 500 이하 배열에 암호코드
2. 1개 이상의 암호코드 존재(비정상적인 암호코드 포함될 수도 있음)
3. 암호코드들 정상적인 암호코드인지 확인 암호코드의 숫자 합 출력
4. 총 소요시간 적을 수록 성능 좋은 것

1. 암호코드가 붙어있지 않다! 일부만 있지도 않다!
2. 암호코드가 길면 숫자하나가 차지하는 길이도 배수로 늘어난다.
    (암호코드의 길이 : 56 112 ...)
3. 16진수

풀이

16진수를 2진수로 바꿔야됨
2진수에서 1로 끝나는 곳 기준으로

'''

# 56보다 작으면 56으로 맞추고 112보다 작으면 앞에 0 넣어서 112로 맞추기!
hex = '0123456789ABCDEF'
hex_to_bin = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',\
       '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']

code = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

def pw_sum(password): # password에 int 리스트 넣어야됨, k는 password몇배수인지
    odd_flag = True
    password_sum = 0
    print_sum = 0
    for i in range(len(password) - 1):
        if odd_flag:
            password_sum += password[i] * 3
            print_sum += password[i]
        else:
            password_sum += password[i]
            print_sum += password[i]
        odd_flag = not odd_flag
    password_sum += password[7]
    print_sum += password[7]
    if password_sum % 10 == 0:
        return print_sum
    return 0

def full_password(password):
    b = 56 - len(password) % 56
    return '0'*b + password
    

def password_dec(password, k):
    r = []
    tmp = ''
    i = 0
    while i < 56*k:
        tmp += password[i]
        i += k
    
    for i in range(8):
        t = ''.join(map(str, list(tmp[i*7:i*7+7])))
        r.append(code.index(t))
    return r

def split_zero(s):
    res = []
    i = 0
    while i < len(s):
        a = s[i]
        if a == '0':
            i += 1
            continue
        tmp = ''
        while i < len(s) and a != '0':
            tmp += s[i]
            i += 1
             

        

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    a = [input().rstrip() for _ in range(n)]
    last = ''
    set1 = set()
    answer = 0

    for a1 in a:
        if a1 == last:
            continue
        l = 0
        splits = split_zero(a1)
        for s in splits:
            if s != '':
                set1.add(s)
        last = a1    

    # 2진수로 변환하고 앞에 0으로 채우기
    for h in set1:
        password = ''
        for i in h:
            password += hex_to_bin[hex.index(i)]
        password = password.strip('0')
        
        password = full_password(password)
        password = password_dec(password, len(password)//56)
        answer = pw_sum(password)
        if answer:
            break

    print(f'#{tc} {answer}')

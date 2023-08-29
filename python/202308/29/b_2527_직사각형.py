'''
직사각형

두개의 꼭짓점 좌표로 표현된 직사각형
두 직사각형이 직사각형/선분/점이 겹칠 수도 있고
겹치지 않을 수도 있다.
직사각형/선분/점/겹치지않음
a   /   b   /   c   /   d

4개의 테스트케이스
'''

for _ in range(4):
    l1, d1, r1, u1, l2, d2, r2, u2 = map(int, input().split())
    
    if r2 < l1 or l2 > r1 or u2 < d1 or d2 > u1:
        print('d')
    elif (l1==r2 and d1==u2) or (l1==r2 and u1==d2) \
        or (l2==r1 and d2==u1) or (l2==r1 and u2==d1):
        print('c')
    elif l1==r2 or l2==r1 or u1==d2 or u2==d1:
        print('b')
    else:
        print('a')

    


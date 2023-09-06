'''
주식
백준 11501
난이도 실버 2

1. 주식하나를 산다.
2. 원하는 만큼 가지고 있는 주식을 판다.
3. 아무것도 안한다.


'''

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    price = list(map(int, input().split()))
    max_p = 0
    ans = 0
    
    for i in range(n-1, -1, -1):
        if max_p < price[i]:
            max_p = price[i]
        else:
            ans += max_p - price[i]
    print(ans)
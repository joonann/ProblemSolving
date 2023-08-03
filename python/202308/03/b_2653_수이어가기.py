# 수 이어가기
# 백준 2653
# 난이도 : 실버 5

# 첫번째 수 주어지고 그보다 작은 수 하나를 정했을 때
# 100 62 38 24 14 10 4 6 처럼 연속해서 빼는 수 배열 
# 개수 최대일 경우 구하기


# 브루트포스 말고 더 효율적인 방법이 없을까 고민해보다가 포기함

n = int(input())
answer = []
max_count = 0

for i in range(1, n + 1):
    list = [n, i]
    count = 2
    while list[-2] - list[-1] >= 0:
        list.append(list[-2] - list[-1])
        count += 1
    if max_count < count:
        max_count = count
        answer = list

print(max_count)
print(' '.join(map(str, answer)))
        
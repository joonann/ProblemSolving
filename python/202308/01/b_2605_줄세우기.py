# 줄 세우기
# 백준 2605
# 난이도 : 브론즈 2

# 1번 학생부터 새치기 하는 인원 수
n = int(input())
arr = list(map(int, input().split()))
line = []

for i in range(1, n + 1):
    if arr[i - 1] == 0:
        line.append(i)
    else:
        line.insert(arr[i - 1] * -1, i)

a = ' '.join(map(str, line))
print(a)
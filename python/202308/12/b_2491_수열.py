# 수열
# 백준 2491
# 난이도 : 실버 4

# n개의 나열된 숫자
# 오름차순 / 내림차순 가장 긴 길이 구하기
n = int(input())
nums = list(map(int, input().split()))
dp1, dp2 = [1]*n, [1]*n
for i in range(1, n):
    if nums[i] <= nums[i-1]:
        dp1[i] = dp1[i-1] + 1
    if nums[i] >= nums[i-1]:
        dp2[i] = dp2[i-1] + 1
print(max(max(dp1), max(dp2)))

# 입력배열 nums 1 2 2 3 2 4 5 6 9 1 
# 내림차순 dp1  1 1 2 1 2 1 1 1 1 2
# 오름차순 dp2  1 2 3 4 1 2 3 4 5 1
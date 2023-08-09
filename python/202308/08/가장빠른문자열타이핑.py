# 가장 빠른 문자열 타이핑
# SWEA 
# 난이도 : D4

t = int(input())
for tc in range(1, t+1):
    str1, str2 = input().split()
    len1, len2 = len(str1), len(str2)
    count = 0
    j = 0

    for i in range(len1):
        count += 1
        if j < len2 and str1[i] == str2[j]:
            j += 1
            if j == len2:
                count = count - j + 1
            else:
                continue
        j = 0

    print(f'#{tc} {count}')

# t = int(input())

# for tc in range(1, t+1):
#     str1, str2 = input().split()
#     count = str1.count(str2)
#     print(f'#{tc} {len(str1) - count * (len(str2) - 1)}')
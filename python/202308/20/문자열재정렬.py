# 문자열 재정렬

s = list(input())
s.sort()

print(s)
num = 0
for a in s:
    if '0' <= a <= '9':
        num += int(a)
    else:
        print(a, end='')
print(num)
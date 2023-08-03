def print_subset(bit, arr, n):
    total = 0
    for i in range(n):
        if bit[i]:
            total += arr[i]
    print(bit, total)

arr = [1, 2, 3, 4]
bit = [0, 0, 0, 0]

for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                # print_subset(bit, arr, 4)

arr = [1, 2, 3, 4, 5, 6]

n = len(arr)
count= 0
for i in range(2**n): # 2의 n제곱 번 순회
    print('현재 집합 :', end=' ')
    for j in range(n): # arr에 있는 인덱스 하나씩 대입
        if i & (1<<j): # i 숫자를 2진수로 바꿨을 때 010100 일 때 2, 4만 포함
                        # 왜냐하면 (1<<j)가 000001을 왼쪽으로 하나씩 밀어낸 2진수
            print(arr[j], end=", ")
    print()
    count += 1 # 조합마다 count 1씩 증가
print()
print('count:', count)


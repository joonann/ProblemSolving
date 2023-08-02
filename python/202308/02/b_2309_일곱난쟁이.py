# 일곱난쟁이
# 백준 2309
# 난이도 : 브론즈 1

heights = []
fake_total = -100
for _ in range(9): 
    a = int(input())
    heights.append(a)
    fake_total += a

for i in range(9):
    fake_one = heights[i]
    fake_two = fake_total - fake_one
    if fake_two in heights[i + 1:9]:
        heights.remove(fake_one)
        heights.remove(fake_two)
        heights.sort()
        for d in range(7):
            print(heights[d])
        break

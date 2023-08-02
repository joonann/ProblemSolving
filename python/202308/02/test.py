n = 2
m = 4
arr = [[0]*m for _ in range(n)]
arr2 = [[0]*m]*n 
# >> 하나의 리스트를 여러 군데에서 참조하기 때문에
# >> 위의 방법으로 만들어야 됨!
arr[0][0] = 1
arr2[0][0] = 1
print(arr)
print(arr2)
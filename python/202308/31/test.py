arr = [[1, 1], [2, 1], [3, 2], [3, 1], [2, 3], [1, 2], [3, 3], [2, 2], [1, 3]]
arr.sort(key=lambda x: (x[0], x[1]))
print(arr)

arr.sort(key=lambda x: [x[1], x[0]])
print(arr)